from django.db import models

# Create your models here.
class Details (models.Model):
    student_name = models.CharField(max_length=225)
    student_attendence = models.IntegerField(null=True)
    student_Email = models.EmailField(max_length=33)
    student_contactNo = models.IntegerField(null=True)

    def __str__(self):
        return self.student_name
    class Meta:
        db_table = 'Personal_details'