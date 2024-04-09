from django.db import models

# Create your models here.
class login(models.Model):
    user_id = models.CharField(max_length=12)
    password = models.CharField(max_length=115)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'loginform'