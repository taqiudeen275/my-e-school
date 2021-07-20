from django.db import models
from academics.models import  Semester,Academic_year,Subject,Class,Staff,FormMaster
from student.models import Student

class Result(models.Model):
  semester = models.ForeignKey(Semester, on_delete=models.CASCADE,null=True,blank=True)
  academic_year = models.ForeignKey(Academic_year, on_delete=models.SET_NULL, null=True, blank=True)
  time = models.DateField(auto_now=True)

  class Meta:
    unique_together = [ 'semester', 'academic_year']

  def __str__(self):
    return f'{str(self.semester)} {str(self.academic_year)} results'


def score_grade(score):
  if score >= 80:
    return 'A1'
  if 71 <= score <= 79:
    return 'B2'
  if 66 <= score <=70:
    return 'B3'
  if 61 <= score <=65:
    return 'C4'
  if 56 <= score <=60:
    return 'C5'
  if 50 <= score <=55:
    return 'C6'
  if 46 <= score <=49:
    return 'D7'
  if 40 <= score <=45:
    return 'E8'
  if 0 <= score <=39:
    return 'F9'

def score_remarks(score):
  if score >= 80:
    return 'Excellent'
  if 71 <= score <= 79:
    return 'Very Good'
  if 66 <= score <=70:
    return 'Good'
  if 61 <= score <=65:
    return 'Good Credit'
  if 56 <= score <=60:
    return 'Good Credit'
  if 50 <= score <=55:
    return 'Credit'
  if 46 <= score <=49:
    return 'Pass'
  if 40 <= score <=45:
    return 'Pass'
  if 0 <= score <=39:
    return 'Fail'



class SubjectResult(models.Model):
    subject_master = models.ForeignKey(Staff, related_name='subject_result', on_delete=models.CASCADE, null=True,blank=True)
    student = models.ForeignKey(Student, related_name='subject_result', on_delete=models.CASCADE)
    clas_s = models.ForeignKey(Class, related_name='subject_result', on_delete=models.CASCADE, null=True,blank=True)
    result_for = models.ForeignKey(Result, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test_1_score = models.IntegerField(default=0)
    test_2_score = models.IntegerField(default=0)
    mid_semester_score = models.IntegerField(default=0)
    exam_mark = models.IntegerField(default=0)
    absent = models.BooleanField(default=False)
    submitted = models.BooleanField(default=False)
    position_in_subject = models.CharField(max_length=10, default=' - ')
    class Meta:
      ordering = ['subject']

    def __str__(self):
      return f'{self.student} {self.subject} {self.result_for}'
  
    def exam_score(self):
      exam_score_decimal = ( self.exam_mark / 100 ) * 70 
      return round(exam_score_decimal, ndigits=1)   

    def class_score(self):
      class_score_decimal = (self.test_1_score +self.test_2_score + self.mid_semester_score) / 100 * 30
      return round(class_score_decimal,ndigits=1)

    def total_score(self):  
      total_score_deciaml = self.exam_score() + self.class_score()
      return round(total_score_deciaml)

    def grade(self):
      return score_grade(self.total_score())

    def remarks(self):
      return score_remarks(self.total_score())
  
class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name='report_card', on_delete=models.CASCADE)
    subjects_result = models.ManyToManyField(SubjectResult, related_name='reportCard')
    result_for = models.ForeignKey(Result, related_name='reportCard', on_delete=models.CASCADE)
    conduct = models.CharField(max_length=500, blank=True, null=True)
    attitude = models.CharField(max_length=500, blank=True, null=True)
    interest = models.CharField(max_length=500, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    overall_total = models.IntegerField(null=True, blank=True)
    position_in_class = models.CharField(max_length=10, null=True, blank=True)
    clas_s = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True,null=True, related_name='report_cards')

    class Meta:
        unique_together = ['student', 'result_for']
    def average_score(self):
      total_marks = self.overall_total
      av_mark = total_marks / self.subjects_result.all().count()
      return round(av_mark, ndigits=2)

    def __str__(self):
      return f'{self.student} {self.result_for}'

class AboutStudent(models.Model):
  form_master = models.ForeignKey(FormMaster, on_delete=models.SET_NULL, null=True, blank=True)
  student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='about')
  semester = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='about_student')
  conduct = models.CharField(max_length=500, blank=True, null=True)
  attitude = models.CharField(max_length=500, blank=True, null=True)
  interest = models.CharField(max_length=500, blank=True, null=True)
  remarks = models.CharField(max_length=500, blank=True, null=True)
  submitted = models.BooleanField(default=False)
  class Meta:
        unique_together = ['student', 'semester']
  def __str__(self):
    return f"{self.student}'s about"