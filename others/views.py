from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from account.models import User

@login_required
def basicsView(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    # Load models
    staff_positions = StaffPosition.objects.all()
    about_staff = AboutStaff.objects.all()
    notice_board = NoticeBoard.objects.all()
    school_history = SchoolHistory.objects.all()

    # Load Forms
    staff_positionForm = StaffPositionForm(request.POST or None)
    about_staffForm = AboutStaffForm(request.POST or None)
    notice_boardForm = NoticeBoardForm(request.POST or None, request.FILES or None)
    school_historyForm = SchoolHistoryForm(request.POST or None,request.FILES or None)

    context = {
        'staffPositions':staff_positions,
        'aboutStaff':about_staff,
        'noticeBoard':notice_board,
        'schoolHistory':school_history,
        # forms
        'spForm': staff_positionForm,
        'asForm': about_staffForm,
        'nbForm': notice_boardForm,
        'shForm': school_historyForm,
        'title':'Others',
    }
    template_name = 'others/basics.html'
    return render(request, template_name, context)

# Save or Create Views

@login_required
def saveAS(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    asForm =AboutStaffForm(request.POST or None)
    if request.method == 'POST':
        if asForm.is_valid():
            asForm.save()
            messages.success(request, 'About Staff created successfully')
            return redirect('others:basics')

@login_required
def saveSP(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    spForm = StaffPositionForm(request.POST or None)
    if request.method == 'POST':
        if spForm.is_valid():
            spForm.save()
            messages.success(request, 'Staff Position created successfully')
            return redirect('others:basics')

@login_required        
def saveNB(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    nbForm = NoticeBoardForm(request.POST or None)
    if request.method == 'POST':
        if nbForm.is_valid():
            nbForm.save()
            messages.success(request, 'created successfully')
            return redirect('others:basics')

@login_required
def saveSH(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    shForm = SchoolHistoryForm(request.POST or None)
    if request.method == 'POST':
        if shForm.is_valid():
            shForm.save()
            messages.success(request, 'created successfully')
            return redirect('others:basics')

#  Delete Views

@login_required
def deleteSP(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(StaffPosition, id=id)
        item_to_delete.delete()
        messages.success(request, 'deleted successfully')
        return redirect('others:basics')

@login_required
def deleteAS(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(AboutStaff, id=id)
        item_to_delete.delete()
        messages.success(request, 'deleted successfully')
        return redirect('others:basics')

@login_required
def deleteNB(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(NoticeBoard, id=id)
        item_to_delete.delete()
        messages.success(request, 'deleted successfully')
        return redirect('others:basics')

@login_required
def deleteSH(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(SchoolHistory, id=id)
        item_to_delete.delete()
        messages.success(request, 'deleted successfully')
        return redirect('others:basics')

@login_required
def aboutStaffView(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    aS = get_object_or_404(AboutStaff, id=id)
    asForm = AboutStaffForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if asForm.is_valid():
            form.save()
            messages.info(request, 'added successfully')
            return redirect('others:basics')

    context = {
        'form': asForm,
        'asd': aS,
        'title':'About Staff',
    }
    template_name = 'others/asd.html'
    return render(request, template_name, context)

@login_required    
def uas(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    aS = get_object_or_404(AboutStaff, id=id)
    form = AboutStaffForm(request.POST or None,request.FILES or None,instance=aS)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'updated successful')
            return redirect('others:basics')

    context = {
        'aboutStaff': aS,
        'form': form,
        'title':'Update About Staff',
    }
    return render(request, 'others/uas.html', context)

@login_required
def noticeBoardfView(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    nb = get_object_or_404(NoticeBoard, id=id)
    nbForm = NoticeBoardForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, 'added successfully')
            return redirect('others:basics')

    context = {
        'form': nbForm,
        'nbd': nb,
        'title':'Notice Board',
    }
    template_name = 'others/nbd.html'
    return render(request, template_name, context)

@login_required    
def unb(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    nb = get_object_or_404(NoticeBoard, id=id)
    form = NoticeBoardForm(request.POST or None,request.FILES or None,instance=nb)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'updated successful')
            return redirect('others:basics')

    context = {
        'nb': nb,
        'form': form,
        'title':'Update Notice Board',
    }
    return render(request, 'others/unb.html', context)

@login_required
def schoolHistoryView(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    shd = get_object_or_404(SchoolHistory, id=id)
    shForm = SchoolHistoryForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, 'added successfully')
            return redirect('others:basics')

    context = {
        'shForm': shForm,
        'shd': shd,
        'title':'School History',
    }
    template_name = 'others/shd.html'
    return render(request, template_name, context)

@login_required    
def ush(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    sh = get_object_or_404(SchoolHistory, id=id)
    form = SchoolHistoryForm(request.POST or None,request.FILES or None,instance=sh)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'updated successful')
            return redirect('others:basics')

    context = {
        'sh': sh,
        'form': form,
        'title':'Update School History',
    }
    return render(request, 'others/ush.html', context)

@login_required
def noticeBoardaView(request):
    user = request.user
    if user.user_type  == 'guest':
        return redirect('home:index')
    noticeBoard =  NoticeBoard.objects.all()
    context = {
       'title':'Notice Board',
        'noticeBoard': noticeBoard,
    }
    return render(request, 'others/noticeBoard.html', context)

@login_required
def noticeBoardPost(request, id):
    user = request.user
    if user.user_type  == 'guest':
        return redirect('home:index')
    nb = get_object_or_404(NoticeBoard, id=id)
    context = {
       
        'nbd': nb,
        'title':nb.title,
    }
    return render(request, 'others/noticeBoardPost.html', context)

@login_required
def aboutSchoolView(request):
    # sh -- school history
    sh =  SchoolHistory.objects.all()
    context = {
       
        'sh': sh,
        'title':'About School',
    }
    return render(request, 'others/aboutSchool.html', context)

@login_required
def aboutStaffaView(request):
    # am -- about master
    am =  AboutStaff.objects.all()
    context = {
        'am': am,
        'title':'About Staff',
    }
    return render(request, 'others/aboutStaff.html', context)

@login_required
def aboutSchoolPost(request, id):
    sh = get_object_or_404(SchoolHistory, id=id)
    context = {
       
        'shd': sh,
        'title':sh.title,
    }
    return render(request, 'others/aboutSchoolPost.html', context)