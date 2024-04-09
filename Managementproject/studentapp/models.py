from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.IntegerField(primary_key=True)
    student_name=models.CharField(max_length=225)
    student_attendence=models.IntegerField()
    student_Email=models.EmailField(max_length=33)
    student_contactNo=models.IntegerField(null=False)
    RADIO_CHOICES=[
        ('male','Male'),
        ('female','Female'),
    ]
    Student_gender=models.CharField(max_length=20,choices=RADIO_CHOICES,null=True)
    SELECT_CHOICES=[
        ('Java','Java'),
        ('Python','Python'),
    ]
    student_Course=models.CharField(max_length=10,choices=SELECT_CHOICES,null=True)
    student_photo=models.ImageField()
    student_assignment=models.FileField()

    def __str__(self):
        return self.student_id

    class Meta:
        db_table='student_db'

