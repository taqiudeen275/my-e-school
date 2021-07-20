from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def index(request): 
    user = request.user
    if user.user_type == 'staff':
        return redirect('staffUser:home')
    if user.user_type == 'parent':
        return redirect('parentUser:index')
    if user.user_type == 'student':
        return redirect('studentUser:index')
    template = 'home/index.html'

    return render(request, template, {'title':'home',})
