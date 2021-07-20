from django.shortcuts import render,redirect,get_object_or_404
from result.models import ReportCard,Result
from parent.models import Parent
from studentUser.models import StudentUser
from account.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def studentReportCards(request):
    user = request.user
    if user.user_type  != 'student':
        return redirect('home:index')
    studentUser = get_object_or_404(StudentUser, user=request.user)
    reportCards = ReportCard.objects.filter(student=studentUser.student)
    context={
        'reportCards': reportCards,
        'studentUser':studentUser,
    }
    return render(request, 'messages/studentReportCards.html', context)

@login_required
def reportCard(request, id):
    user = request.user
    if user.user_type  != 'student':
        return redirect('home:index')
    reportCard = ReportCard.objects.filter(id=id)[0]
    context={
        'student':reportCard.student,
        'reportCard': reportCard,
    }   
    return render(request, 'messages/reportCard.html', context)

@login_required
def parentReportCards(request):
    user = request.user
    if user.user_type  != 'parent':
        messages.error(request, 'You are not a parent')
        return redirect('home:index')
    parent = get_object_or_404(Parent, user=user)
    wards = parent.student.all()
    print(wards)
    context={
        'reportCard': reportCard,
        'students': wards,
    }
    return render(request, 'messages/parentReportCards.html', context)

    
