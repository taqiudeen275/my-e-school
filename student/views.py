from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Student
from .forms import  *
from academics.models import Class
from django.db.models import Count,Q
from django.contrib.auth.decorators import login_required

@login_required
def students(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    student = Student.objects.all()

    classSearchforms = ClassStudentSearchForm()
    student_form = StudentSearchForm()
    form = StudentForm(request.POST or None, request.FILES or None)

    cls_name = request.GET.get('class_info', None)
    all_student = request.GET.get('all_student', None)
    first_name = request.GET.get('first_name',None)
    last_name = request.GET.get('last_name',None)
    class_info = request.GET.get('class_info',None)

    if first_name and last_name and class_info:
        qs = Student.objects.filter(first_name__iexact=first_name,last_name__iexact=last_name,clas_s=class_info)
    elif first_name and last_name:
        qs = Student.objects.filter(first_name__iexact=first_name,last_name__iexact=last_name)
    elif cls_name:
        qs = Student.objects.filter(clas_s=cls_name)
    
    elif all_student:
            qs = Student.objects.all()

    else:
        qs = Student.objects.order_by('-id')


    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, 'Student added successfully')
            return redirect('student:students')
    context = {
        'form': form,
        'classSearcForm': classSearchforms,
        'students': qs,
        'sform': student_form,
        'title':'All Students',
    }
    template_name = 'student/students.html'
    return render(request, template_name, context)

@login_required
def studentView(request, id):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, 'Student added successfully')
            return redirect('student:student')

    context = {
        'form': form,
        'student': student,
        'title': student,
    }
    template_name = 'student/student.html'
    return render(request, template_name, context)

@login_required
def deleteStudent(request, id):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Student, id=id)
        item_to_delete.delete()
        messages.info(request, 'Student deleted successfully')
        return redirect('student:students')

@login_required
def student_edit(request, id):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None,request.FILES or None,instance=student)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'Student info updated successful')
            return redirect('student:students')

    context = {
        'student': student,
        'form': form,
    }
    return render(request, 'student/studentedit.html', context)
