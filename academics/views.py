from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import * 
from student.models import House
from student.forms import HouseForm
from django.contrib.auth.decorators import login_required
from staffUser.models import StaffIDCode
from student.models import Student
from result.models import Result
from result.forms import ResultForm

@login_required
def basics(request): 
    user = request.user
    if user.user_type  != 'staff':
        messages.error(request, 'You are not a staff')
        return redirect('home:index')
    programs = Programme.objects.all()
    level = Level.objects.all()
    staffId = StaffIDCode.objects.all()
    klass = Class.objects.all()
    batch = Batch.objects.all()
    semester = Semester.objects.all()
    academic_year = Academic_year.objects.all()
    subject = Subject.objects.all()
    formMaster = FormMaster.objects.all()
    houses = House.objects.all()
    result_for = Result.objects.all()
    # forms
    programForm =ProgrammeForm(request.POST or None)
    houseForm = HouseForm(request.POST or None)
    resultForm = ResultForm(request.POST or None)
    levelForm = LevelForm(request.POST or None)
    klassForm = ClassForm(request.POST or None)
    batchForm = BatchForm(request.POST or None)
    semesterForm = SemesterForm(request.POST or None)
    academic_yearForm = AcademicYearForm(request.POST or None)
    subjectForm = SubjectForm(request.POST or None)
    staffidform = StaffIDCodeForm(request.POST or None)
    formMasterForm = FormMasterForm(request.POST or None)
    
    context = {
        'result_for':result_for,
        'programs': programs,
        'levels': level,
        'classes': klass,
        'batches': batch,
        'semesters': semester,
        'academic_years': academic_year,
        'subjects':subject,
        'houses':houses,
        'staffId':staffId,
        # 'formMasters':formMaster,
        #forms
        'programForm': programForm,
        'levelForm': levelForm,
        'classForm': klassForm,
        'batchForm': batchForm,
        'semesterForm': semesterForm,
        'academic_yearForm': academic_yearForm,
        'subjectForm':subjectForm,
        'houseForm':houseForm,
        'staffIdform':staffidform,
        'creatResultForm':resultForm,
        'title': 'Basics',

    }
    template_name='academics/basics.html'
    return render(request, template_name,context)

@login_required
def saveProgram(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    programForm =ProgrammeForm(request.POST or None)
    if request.method == 'POST':
        if programForm.is_valid():
            programForm.save()
            messages.info(request, 'Pragram created successfully')
            return redirect('academics:basics')

@login_required
def saveLevel(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    levelForm = LevelForm(request.POST or None)
    if request.method == 'POST':
        if levelForm.is_valid():
            levelForm.save()
            messages.info(request, 'Level created successfully')
            return redirect('academics:basics')

@login_required        
def saveClass(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    klassForm = ClassForm(request.POST or None)
    if request.method == 'POST':
        if klassForm.is_valid():
            klassForm.save()
            messages.info(request, 'Class created successfully')
            return redirect('academics:basics')

@login_required        
def saveResultFOr(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    resultForm = ResultForm(request.POST or None)
    if request.method == 'POST':
        if resultForm.is_valid():
            resultForm.save()
            messages.info(request, 'Results created successfully')
            return redirect('academics:basics')

@login_required
def saveBatch(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    batchForm = BatchForm(request.POST or None)
    if request.method == 'POST':
        if batchForm.is_valid():
            batchForm.save()
            messages.info(request, 'Batch created successfully')
            return redirect('academics:basics')

@login_required
def saveStaffID(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    staffidform = StaffIDCodeForm(request.POST or None)
    if request.method == 'POST':
        if staffidform.is_valid():
            staffidform.save()
            messages.info(request, 'Staff Id created successfully')
            return redirect('academics:basics')

@login_required
def saveSemester(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    semesterForm = SemesterForm(request.POST or None)
    if request.method == 'POST':
        if semesterForm.is_valid():
            semesterForm.save()
            messages.info(request, 'Semester created successfully')
            return redirect('academics:basics')

@login_required
def saveAy(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    academic_yearForm = AcademicYearForm(request.POST or None)
    if request.method == 'POST':
        if academic_yearForm.is_valid():
            academic_yearForm.save()
            messages.info(request, 'Academic year created successfully')
            return redirect('academics:basics')
@login_required
def saveSubject(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    subjectForm = SubjectForm(request.POST or None)
    if request.method == 'POST':
        if subjectForm.is_valid():
            subjectForm.save()
            messages.info(request, 'Subject created successfully')
            return redirect('academics:basics')

@login_required
def saveHouse(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    houseform = HouseForm(request.POST or None)
    if request.method == 'POST':
        if houseform.is_valid():
            houseform.save()
            messages.info(request, 'House created successfully')
            return redirect('academics:basics')

@login_required
def deleteProgram(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Programme, id=id)
        item_to_delete.delete()
        messages.info(request, 'Program deleted successfully')    
        return redirect('academics:basics')

@login_required
def deleteResult(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Result, id=id)
        item_to_delete.delete()
        messages.info(request, 'Results deleted successfully')    
        return redirect('academics:basics')

@login_required
def deleteLevel(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Level, id=id)
        item_to_delete.delete()
        messages.info(request, 'Level deleted successfully')
        return redirect('academics:basics')

@login_required
def deleteHouse(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(House, id=id)
        item_to_delete.delete()
        messages.info(request, 'House deleted successfully')
        return redirect('academics:basics')


@login_required
def deleteBatch(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Batch, id=id)
        item_to_delete.delete()
        messages.info(request, 'Batch deleted successfully')
        return redirect('academics:basics')

@login_required
def deleteClass(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Class, id=id)
        item_to_delete.delete()
        messages.info(request, 'Class deleted successfully')
        return redirect('academics:basics')

@login_required
def deleteStaffId(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(StaffIDCode, id=id)
        item_to_delete.delete()
        messages.info(request, 'Staff id deleted successfully')
        return redirect('academics:basics')

@login_required
def deleteSubject(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Subject, id=id)
        item_to_delete.delete()
        messages.info(request, 'Subject deleted successfully')
        return redirect('academics:basics')

#academic year
@login_required
def deleteAy(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Academic_year, id=id)
        item_to_delete.delete()
        messages.info(request, 'Academic year deleted successfully')
        return redirect('academics:basics')

@login_required
def deleteSemester(request, id):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    if request.method == "POST":
        item_to_delete = get_object_or_404(Semester, id=id)
        item_to_delete.delete()
        messages.info(request, 'Semester deleted successfully')
        return redirect('academics:basics')

@login_required
def classChange(request):
    user = request.user
    if user.user_type  != 'staff':
        return redirect('home:index')
    students = Student.objects.filter(completed=False)
    for student in students:
        if student.form == 3:
            student.completed = True
            student.save()
        else:
            student.form += 1
            student.save()
    messages.info(request, 'Student Classes changed successfully')
    return redirect('academics:basics')