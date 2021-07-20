from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from .models import Result,SubjectResult,ReportCard
# from .forms import Result
from student.models import Student
from django.contrib import messages
from staffUser.forms import SearchByRF
from staffUser.views import position_prefix
from django.contrib.auth.decorators import login_required
from academics.models import Class,Staff,FormMaster
from django.db.utils import IntegrityError
from .models import *
from .forms import *

def get_position(semester, clas_s, student, subject):
  q = [item.total_score() for item in SubjectResult.objects.filter(result_for=semester, clas_s=clas_s, subject=subject)]
  sorted(q,reverse=True)
  sq = get_object_or_404(SubjectResult, result_for=semester, student=student, clas_s=clas_s, subject=subject)
  position_in_subject = q.index(sq.total_score()) + 1
  return position_in_subject

@login_required
def results_index(request):
  user = request.user
  if user.user_type  != 'staff':
        return redirect('home:index')
  qform =SearchByRF()
  results = Result.objects.all()
  students = Student.objects.filter(completed=False)
  student_id = request.POST.get('stu', None)
  result_for = request.GET.get('academic_year', None)
  
  
  query = False
  if result_for:
    students = Student.objects.filter(completed=False)
    result_info = get_object_or_404(Result, id=result_for)
    query = True
  

  student_results = False
  if request.method == "POST":
    student_id = request.POST.get('stu', None)
  student = False
  if student_id:
    student_results = get_list_or_404(SubjectResult,student=student_id, result_for=result_for)
    student = get_object_or_404(Student, id=student_id)
  context = {
    'title':'Results',
    'query':query,
    'results':results,
    'students':students,
    'student':student,
    'qform':qform,
    'result_for':result_for,
    'student_results':student_results,
  }

  if result_for:
    context.update({'result_info': result_info})

  return render(request, 'results/index.html', context)

@login_required
def releaseReportCards(request, result_for):
  user = request.user
  if user.user_type  != 'staff':
        return redirect('home:index')
  result_for = get_object_or_404(Result,id=result_for)
  students = Student.objects.filter(completed=False)
  for student in students:
    # sr -- student report
    try:
      sr = ReportCard.objects.create(student=student, result_for=result_for)
    except IntegrityError:
      messages.success(request, 'Report card already created')
      return redirect('results:home')
    subjects_result = SubjectResult.objects.filter(result_for=result_for, student=student)
    overall_total = 0
    for result in subjects_result:
      sr.subjects_result.add(result)
      overall_total += result.total_score()
      result.submitted = True
      result.save()
    sr.overall_total = overall_total
    sr.clas_s = student.clas_s 
    sr.save()
  # om overall marks
  for clas_s in Class.objects.filter():
    om = [marks.overall_total for marks in ReportCard.objects.filter(clas_s=clas_s, result_for=result_for)]
    om.sort(reverse=True)
    for student in clas_s.students.all():
      # sr -- student report card
      sr = get_object_or_404(ReportCard, student=student, result_for=result_for)
      position_in_class = om.index(sr.overall_total) + 1
      sr.position_in_class = position_prefix(str(position_in_class))
      sr.save()
  messages.success(request, 'Report cards created successfully')
  return redirect('results:home')


@login_required
def create_aboutStudent(request):
    user = request.user
    if user.user_type  != 'staff':
          return redirect('home:index')
    staff = get_object_or_404(Staff, user=request.user)
    form_master = get_object_or_404(FormMaster, staff=staff)
    clas = form_master.clas_s 
    students = []
  
    student = get_list_or_404(Student, clas_s=clas)
    if type(student) == list :
        for i in student:
            students.append(i)
    else:
        students.append(student)

    if request.method == 'POST':
          #after visiting the second page
          if 'finish' in request.POST:
              form = CreateResultStaffUser(request.POST)
              if form.is_valid():
                  result_for = form.cleaned_data['result_for']
                  students = request.POST['students']
                  abouts = []
                  for student in students.split(','):
                      stu = Student.objects.get(pk=student)
                      check = AboutStudent.objects.filter(semester=result_for, student=stu, form_master=form_master).first()
                      if not check:
                          abouts.append(
                              AboutStudent(
                                  semester=result_for,
                                  student=stu,
                                  form_master=form_master
                              )
                          )
                  AboutStudent.objects.bulk_create(abouts)
                  return redirect('results:fill_abouts', result_for.id)

          #after choosing students
          id_list = request.POST.getlist('students')
          if id_list:
              form = CreateResultStaffUser()
              studentlist = ','.join(id_list)
              return render(request, 'results/create_about_2.html', {"students": studentlist, "form": form, "count":len(id_list)})
          else:
              messages.warning(request, "You didnt select any student.")
      
    return render(request, 'results/create_about.html', {"students": students, 'form_master': form_master, 'title':'Fill About Student',})


@login_required
def fill_abouts(request, result_for):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    staff = get_object_or_404(Staff, user=request.user)
    fmstaff = get_object_or_404(FormMaster, staff=staff)
    EditAboutStudent = modelformset_factory(AboutStudent,fields=('conduct', 'attitude', 'interest', 'remarks',), extra=0, can_delete=True)
    form = EditAboutStudent(queryset=AboutStudent.objects.filter(form_master=fmstaff, semester=result_for))
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Result filled successfully')
            return redirect('staffUser:allResults')
        messages.error(request, 'Error in saving')

    return render(request, 'results/fill_about.html', {"formset": form,'title':'About student Form',})


@login_required
def saveAbout(request):
    if request.method == "POST":
        EditAboutStudent = modelformset_factory(AboutStudent,fields=('conduct', 'attitude', 'interest', 'remarks',), extra=0, can_delete=True)
        form = EditAboutStudent(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Result filled successfully')
            return redirect('results:all_about')


@login_required
def all_studentabout_view(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    qform =SearchByRF()
    staff = get_object_or_404(Staff, user=request.user)
    form_master = get_object_or_404(FormMaster, staff=staff)
    abouts = AboutStudent.objects.filter(form_master=form_master)
    result_for = request.GET.get('academic_year', None)
    ay = False
    if result_for:
        abouts = AboutStudent.objects.filter(form_master=form_master, semester=result_for)
        ay = True

    context = {
        'result_for':result_for,
        'ay':ay,
        'qform':qform,
        'staff':staff,
        'abouts': abouts,
        'title':'Students Remarks',
    }
    return render(request, 'results/all_abouts.html', context)


@login_required
def delete_student_remarks(request, id):
  user = request.user
  if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
  item_to_delete = get_object_or_404(AboutStudent, id=id)
  item_to_delete.delete()
  messages.info(request, 'Student remarks deleted successfully')
  return redirect('results:all_about')

@login_required
def add_remarks(request, result_for):
  user = request.user
  if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
  result_for = get_object_or_404(Result,id=result_for)
  staff = get_object_or_404(Staff, user=request.user)
  form_master = get_object_or_404(FormMaster, staff=staff)
  students = Student.objects.filter(clas_s=form_master.clas_s, completed=False)
  for student in students:
    about = get_object_or_404(AboutStudent,semester=result_for, student=student)
    card = get_object_or_404(ReportCard,result_for=result_for, student=student)
    if card and about:
      card.attitude = about.attitude
      card.conduct = about.conduct
      card.interest = about.interest
      card.remarks = about.remarks
      card.save()
      about.submitted = True
      about.save()
    else:
      messages.error(request, 'Students result is not yet submitted wait and try again after results are submitted')
      return redirect('results:all_about')
  messages.info(request, 'Students remarks submitted successfully')
  return redirect('results:all_about')


@login_required
def delete_report_card(request):
  user = request.user
  if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
  if request.method == "POST":
    result_for = request.POST.get('academic_year', None)
    DeleteReportCards = modelformset_factory(ReportCard,fields=('student',), extra=0, can_delete=True)
    form = DeleteReportCards(queryset=ReportCard.objects.filter(result_for=result_for))
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.warning(request, 'Report Cards Deleted successfully')
            return redirect('staffUser:allResults')
       
    return render(request, 'results/delete_report.html', {"formset": form, 'title':'Delete Report Cards',})

@login_required
def delete_reports(request):
    user = request.user
    if user.user_type  != 'staff':
          messages.error(request, 'You are not a staff')
          return redirect('home:index')
    if request.method == "POST":
        DeleteReportCards = modelformset_factory(ReportCard,fields=('student',), extra=0, can_delete=True)
        form = DeleteReportCards(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reports Card Deleted successfully')
            return redirect('results:all_about')