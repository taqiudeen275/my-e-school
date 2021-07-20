from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from academics.forms import StaffUserForm,FormMasterForm,StaffVerifyForm
from academics.models import Staff,FormMaster
from .models import StaffIDCode
from account.form import ChangeUTForm
from result.models import SubjectResult,Result
from result.forms import CreateResultStaffUser,EditSubjectResults
from student.models import Student
from django.forms import modelformset_factory
from .forms import SearchByRF
from parent.models import Parent
from account.models import User



@login_required
def staffRegister(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    staff = get_object_or_404(Staff, user=request.user)
    if staff.verified :
        return redirect('staffUser:home')
    instance = get_object_or_404(Staff,user=request.user)
    cform = ChangeUTForm(request.POST or None, instance=request.user)
    form = StaffUserForm(request.POST or None, request.FILES or None,instance=instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully')
            return redirect('staffUser:verify')
    context = {
        'form': form,
        'cform':cform,
        'title':'Staff Registration',
    }
    template_name = 'staffUser/register.html'
    return render(request, template_name, context)


@login_required
def verifyStaff(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    staff = get_object_or_404(Staff, user=request.user)
    staff_code = get_object_or_404(StaffIDCode, current=True)
    form = StaffVerifyForm(request.POST or None)
    cform = ChangeUTForm(request.POST or None, instance=request.user)
    if  staff.verified :
        return redirect('staffUser:home')
    if request.method == 'POST':
        code = request.POST.get('staff_id')
        if code == staff_code.name:
            staff.verified = True
            staff.save()
            messages.success(request, 'Your Account was verified')
            return redirect('staffUser:home')
        else:
            messages.error(request, 'Wrong Id code try again')
            return redirect('staffUser:verify')
    context = {
        'form':form,
        'staff':staff,
        'cform':cform,
        'title':'Staff Verification',
    }
    template_name = 'staffUser/verify.html'
    return render(request, template_name, context)

@login_required
def staffHome(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    staff = get_object_or_404(Staff, user=request.user)
    form = StaffVerifyForm(request.POST or None)
    cform = ChangeUTForm(request.POST or None, instance=request.user)
    if not staff.verified :
        return redirect('staffUser:register')
    context = {
        'staff':staff,
        'form': form,
        'cform': cform,
        'title':'Home',
    }
    if user.is_superuser:
        total_students = Student.objects.all().count()
        total_staff = Staff.objects.all().count()
        total_parent = Parent.objects.all().count()
        total_users = User.objects.all().count()
        total_guest = User.objects.filter(user_type="guest").count()
        total_studentUser = User.objects.filter(user_type="student").count()
        context.update({
            'ts':total_students,
            'tstaff':total_staff,
            'tp':total_parent,
            'tg':total_guest,
            'tu':total_users,
            'tsu':total_studentUser,

        })
    template_name = 'staffUser/index.html'
    return render(request, template_name, context)

@login_required
def create_result(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    staff = get_object_or_404(Staff, user=request.user)
    if not staff.verified :
        return redirect('staffUser:register')
    classes = staff.class_taught.all()
    students = []
    for clas in classes:
        student = get_list_or_404(Student, clas_s=clas)
        if type(student) == list :
            for i in student:
                students.append(i)
        else:
            students.append(student)

    print(students)

    if request.method == 'POST':

        #after visiting the second page
        if 'finish' in request.POST:
            form = CreateResultStaffUser(request.POST)
            if form.is_valid():
                result_for = form.cleaned_data['result_for']
                students = request.POST['students']
                results = []
                for student in students.split(','):
                    stu = Student.objects.get(pk=student)
                    check = SubjectResult.objects.filter(result_for=result_for,subject=staff.subject_taught, student=stu).first()
                    if not check:
                        results.append(
                            SubjectResult(
                                subject_master=staff,
                                result_for=result_for,
                                subject=staff.subject_taught,
                                student=stu,
                                clas_s=stu.clas_s
                            )
                        )
                SubjectResult.objects.bulk_create(results)
                return redirect('staffUser:fill_scores', result_for.id)

        #after choosing students
        id_list = request.POST.getlist('students')
        if id_list:
            form = CreateResultStaffUser()
            studentlist = ','.join(id_list)
            return render(request, 'staffUser/create_results_2.html', {"students": studentlist, "form": form, "count":len(id_list)})
        else:
            messages.warning(request, "You didnt select any student.")
    return render(request, 'staffUser/create_result.html', {"students": students, 'title':'Results',})


@login_required
def fill_results(request, result_for):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    staff = get_object_or_404(Staff, user=request.user)
    if not staff.verified :
        return redirect('staffUser:register')
    EditSubjectResultStaff = modelformset_factory(SubjectResult,fields=('test_1_score', 'test_2_score', 'mid_semester_score', 'exam_mark', 'absent'), extra=0, can_delete=True)
    form = EditSubjectResultStaff(queryset=SubjectResult.objects.filter(subject_master=staff, result_for=result_for))
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Result filled successfully')
            return redirect('staffUser:allResults')
        messages.error(request, 'Error in saving')

    return render(request, 'staffUser/fill_scores.html', {"formset": form, 'title':'Results Form',})
@login_required
def saveSubjectResult(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    if request.method == "POST":
        EditSubjectResultStaff = modelformset_factory(SubjectResult,fields=('test_1_score', 'test_2_score', 'mid_semester_score', 'exam_mark', 'absent'), extra=0, can_delete=True)
        form = EditSubjectResultStaff(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result filled successfully')
            return redirect('staffUser:allResults')

@login_required
def all_results_view(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    qform =SearchByRF()
    staff = get_object_or_404(Staff, user=request.user)
    if not staff.verified :
        return redirect('staffUser:register')
    results = SubjectResult.objects.filter(subject_master=staff)
    bulk = {}
    result_for = request.GET.get('academic_year', None)
    ay = False
    if result_for:
        results = SubjectResult.objects.filter(subject_master=staff, result_for=result_for)
        ay = True
         
    for result in results:
        subjects = []
        for subject in results:
            if subject.student == result.student:
                subjects.append(subject)
            

        bulk[result.student.id] = {
        "student": result.student,
        "subjects": subjects,
        "class_score": result.class_score,
        "exam_score": result.exam_score,
        "total_total": result.total_score
        }

    context = {
        'result_for':result_for,
        'ay':ay,
        "results": bulk,
        'qform':qform,
        'staff':staff,
        'title':'All Results',
        
    }
    return render(request, 'staffUser/results.html', context)

def position_prefix(pos):
    if pos[-1] == '1':
        return f'{pos}st'
    elif pos[-1] == '2':
        return f'{pos}nd'
    elif pos[-1] == '3':
        return f'{pos}rd'
    else:
        return f'{pos}th'
    
@login_required
def assignSubjectPosition(request, result_for):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    staff = get_object_or_404(Staff, user=request.user)
    if not staff.verified :
        return redirect('staffUser:register')
    for clas_s in staff.class_taught.all():
        q = [item.total_score() for item in SubjectResult.objects.filter(result_for=result_for, clas_s=clas_s, subject=staff.subject_taught)]
        q.sort(reverse=True)
        students = Student.objects.filter(clas_s=clas_s)
        for student in students:
            sq = get_object_or_404(SubjectResult, result_for=result_for, student=student, clas_s=clas_s, subject=staff.subject_taught)
            position_in_subject = q.index(sq.total_score()) + 1
            sq.position_in_subject = position_prefix(str(position_in_subject))
            sq.save()
    messages.success(request, 'Position in subject created  successfully')
    return redirect('staffUser:allResults')

                
    