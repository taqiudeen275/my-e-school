from django.shortcuts import render,get_object_or_404,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.models import Student
from .models import StudentUser
from student.forms import  *
from academics.models import Class
from django.db.models import Count,Q
from staffUser.forms import SearchByRF
from account.form import ChangeUTForm
from .form import SearchByCode

@login_required
def studentRegister(request):
    user = request.user
    if user.user_type  != 'student':
        messages.error(request, 'You are not a student')
        return redirect('home:index')
    studentUser = get_object_or_404(StudentUser, user=request.user)
    if studentUser.verified :
        return redirect('studentUser:home')
    searchById = SearchByCode(request.POST or None)
    cform = ChangeUTForm(request.POST or None, instance=request.user)
    context = {
        'cform':cform,
        'sform':searchById,
        'title': 'Student Registration',
    }
    template_name = 'studentUser/register.html'
    return render(request, template_name, context)

@login_required
def verifyStudent(request):
    context = {'title': 'Stdent Verification',}
    if request.method == "POST":
        code = request.POST.get('code', None)
        print(code)
        student = Student.objects.filter(my_id=code)
        if student.exists():
            student = student[0]
            if student.user:
                messages.error(request, 'The is already a user with that ID')
                return redirect('studentUser:register')
            context.update({'student':student})
            template_name = 'studentUser/verify.html'
            return render(request, template_name, context)
        else:
            messages.success(request, 'Incorrect ID')
            return redirect("studentUser:register")

def verified(request, student):
    user = request.user
    if user.user_type  != 'student':
        messages.error(request, 'You are not a student')
        return redirect('studentUser:index')
    studentUser = get_object_or_404(StudentUser, user=user)
    student = get_object_or_404(Student, id=student)
    student_user = get_object_or_404(StudentUser, user=request.user)
    student.user = user
    student.save()
    student_user.student = student
    student_user.verified = True
    student_user.save()
    messages.success(request, 'Account verified')
    return redirect("studentUser:index")



@login_required
def studentHome(request):
    user = request.user
    if user.user_type  != 'student':
        messages.error(request, 'You are not a student')
        return redirect('home:index')
    context = {'title': 'Home',}
    template_name = 'studentUser/index.html'
    return render(request, template_name, context)


@login_required
def allStudentID(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    students = Student.objects.filter(completed=False)
    context={
        'students':students,
        'title': 'All Studnts ID',
    }
    return render(request, 'studentUser/allStudentsID.html', context)