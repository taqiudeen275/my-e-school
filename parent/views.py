from django.shortcuts import render,get_object_or_404,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from student.models import Student
from studentUser.models import StudentUser
from student.forms import  *
from academics.models import Class
from django.db.models import Count,Q
from staffUser.forms import SearchByRF
from account.form import ChangeUTForm
from studentUser.form import SearchByCode
from .models import Parent

@login_required
def parentRegister(request):
    user = request.user
    if user.user_type  != 'parent':
        messages.error(request, 'You are not a parent')
        return redirect('home:index')
    parentUser = get_object_or_404(Parent, user=request.user)
    searchById = SearchByCode(request.POST or None)
    cform = ChangeUTForm(request.POST or None, instance=request.user)
    context = {
        'cform':cform,
        'sform':searchById,
        'title':'Parent Registration',
    }
    template_name = 'parentUser/register.html'
    return render(request, template_name, context)

@login_required
def verifyStudent(request):
    user = request.user
    if user.user_type  != 'parent':
        messages.error(request, 'You are not a parent')
        return redirect('home:index')
    context = {}
    if request.method == "POST":
        code = request.POST.get('code', None)
        print(code)
        student = Student.objects.filter(my_id=code)
        if student.exists():
            student = student[0]
            context.update({'student':student})
            template_name = 'parentUser/verify.html'
            return render(request, template_name, context)
        else:
            messages.success(request, 'Incorrect ID')
            return redirect("parentUser:register")

@login_required
def verified(request, student):
    user = request.user
    if user.user_type  != 'parent':
        messages.error(request, 'You are not a Parent')
        return redirect('home:index')
    parentUser = get_object_or_404(Parent, user=user)
    student = get_object_or_404(Student, id=student)
    parentUser.student.add(student)
    parentUser.verified = True
    parentUser.save()
    messages.success(request, 'Account verified')
    return redirect("parentUser:index")



@login_required
def parentHome(request):
    user = request.user
    if user.user_type  != 'parent':
        messages.error(request, 'You are not a parent')
        return redirect('home:index')
    context = {'title':'home',}
    template_name = 'parentUser/index.html'
    return render(request, template_name, context)
