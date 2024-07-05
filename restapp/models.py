from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    address=models.TextField(max_length=20)
    phone=models.CharField(max_length=10)

class BookModel(models.Model):
    book_name=models.CharField(max_length=25)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book_author=models.CharField(max_length=25)
    book_price=models.IntegerField()   

    def __str__(self):
        return self.book_name 
    

class StudentModel(models.Model):
    student_name=models.CharField(max_length=20)  
    admno=models.CharField(max_length=20)
    course=models.CharField(max_length=25) 
    dob=models.DateField() 
    address=models.CharField(max_length=20)


    def __str__(self):
        return self.student_name
class Taskmodel(models.Model):
    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Completed','Completed'),
        ('Approved','Approved'),
    ]
    task_name=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task_title=models.CharField(max_length=20)
    due_date=models.DateField()
    status=models.CharField(max_length=15,default='Pending',choices=STATUS_CHOICES)

    def __str__(self):
        return self.task_name

