from django.shortcuts import render,redirect,get_object_or_404,reverse
from .form import *
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages
from staff.forms import StaffForm 
from academics.models import Staff
from student.models import  Student
from student.forms import StudentForm
from studentUser.models import StudentUser
from parent.models import Parent



def loginView(request):
    if request.user.is_authenticated:
        return redirect(reverse('home:index'))   
    next1 = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if username and password is not None:
                user = authenticate(username=username,password=password)
                login(request,user)
            
                if next1:
                    return redirect(next1)
            return redirect(reverse('home:index'))
    context = {
        'form': form,
        'title': 'Login',
        
    }
    return render(request, 'account/login.html', context)



def signupView(request):
    form = SignupForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect(reverse('home:index'))
    if request.method == 'POST':
        if form.is_valid():
            user =form.save(commit= False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user = authenticate(username=user.username, password=password)
            login(request, user)
            if user.user_type == "Staff":
                return redirect('staffUser:register')
            elif user.user_type == "Student":
                return redirect('studentUser:register')
            elif user.user_type == "Parent":
                return redirect('parentUser:register')
            else:
                return redirect(reverse('home:index'))
    context = {
        'form': form,
        'title': 'Register',
    }
    return render(request, 'account/register.html', context)


def logoutView(request):
    logout(request)
    return redirect(reverse('account:login'))

@login_required
def profile(request):
    form = ProfileForm(request.POST or None,request.FILES or None, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {
        'form': form,
        'title': 'Profile',
    }
    user = request.user
    if user.user_type == 'staff':
        staff = get_object_or_404(Staff, user=request.user)
        if not staff.verified :
            return redirect('staffUser:register')
        staff_form = StaffForm(request.POST or None, instance=staff)
        context.update({'staff_form':staff_form,  'staff':staff})

    if user.user_type == 'student':
        studentUser = get_object_or_404(StudentUser, user=request.user)
        if not studentUser.verified:
            return redirect('studentUser:register')
        student = get_object_or_404(Student, user=request.user)
        student_form = StudentForm(request.POST or None, request.FILES or None, instance=student)
        context.update({'student_form':student_form,  'student':student})

    if user.user_type == 'parent':
        parentUser = get_object_or_404(Parent, user=request.user)
        if not parentUser.verified:
            messages.error(request, 'verify your account')
            return redirect('parentUser:register')
        context.update({'parent':parentUser})
    
    return render(request, 'account/profile.html', context)

@login_required
def change_userType(request):
    form = ChangeUTForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'User Type Changed Sucessfully')
            redirect('home:index')
    return redirect('account:profile')

@login_required    
def saveStaff(request):
    staff = get_object_or_404(Staff, user=request.user)
    form = StaffForm(request.POST or None, request.FILES or None, instance=staff)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Your Staff's info edited sucessfully")
    return redirect('account:profile')
    
@login_required
def saveStudent(request):
    student = get_object_or_404(Student, user=request.user)
    form = StudentForm(request.POST or None, request.FILES or None,  instance=student)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Your Student's info edited sucessfully")
    return redirect('account:profile')