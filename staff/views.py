from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from academics.models import Staff,FormMaster
from academics.forms import FormMasterForm,StaffForm
from django.contrib.auth.decorators import login_required


@login_required
def staffs(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    form = StaffForm(request.POST or None, request.FILES or None)
    staff = Staff.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, 'Staff added successfully')
            return redirect('staff:staffs')
    context = {
        'form': form,
        'staffs': staff,
        'title':'All Teaching Staff',
    }
    template_name = 'staff/staffs.html'
    return render(request, template_name, context)

@login_required
def staffView(request, id):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    staff = get_object_or_404(Staff, id=id)
    form = StaffForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, 'Staff added successfully')
            return redirect('staff:staffs')

    context = {
        'form': form,
        'staff': staff,
        'title': staff,
    }
    template_name = 'staff/staff.html'
    return render(request, template_name, context)

@login_required    
def staff_edit(request, id):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    staff = get_object_or_404(Staff, id=id)
    form = StaffForm(request.POST or None,request.FILES or None,instance=staff)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'Staff info updated successful')
            return redirect('staff:staffs')

    context = {
        'staff': staff,
        'form': form,
        'title':f'Edit {staff}',
    }
    return render(request, 'staff/staffedit.html', context)

@login_required
def deleteStaff(request, id):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Staff, id=id)
        item_to_delete.delete()
        messages.info(request, 'Staff deleted successfully')
        return redirect('staff:staffs')

@login_required
def formMaster(request):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    form = FormMasterForm(request.POST or None)
    formMaster = FormMaster.objects.all()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, 'Form Master added successfully')
            return redirect('staff:formMaster')
    context = {
        'form': form,
        'formMasters': formMaster,
        'title':'Form Master or Mistress',
    }
    template_name = 'staff/formMaster.html'
    return render(request, template_name, context)

@login_required
def deleteformMaster(request, id):
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(FormMaster, id=id)
        item_to_delete.delete()
        messages.info(request, 'Form Master deleted successfully')
        return redirect('staff:formMaster')