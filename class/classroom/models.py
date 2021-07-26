from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    image = models.ImageField(upload_to='room_images', height_field=None, width_field=None, max_length=100,null=True)
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,)
class Joined(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,)
    classroom_code = models.CharField(max_length=200)
    classroom_name = models.CharField(max_length=200)
    classroom_image = models.ImageField(upload_to='Joined', height_field=None, width_field=None, max_length=100,null=True)
class Upload_Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,blank=True)
    task = models.TextField(max_length=1000,blank = True,)
    room_code = models.CharField(max_length=200) 
    # file = models.FileField(blank=True,upload_to='tasks')
    date = models.DateField(null=True)
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,)
    max_points = models.IntegerField(blank = True, null= True)
    due_date = models.DateField(blank=True,null=True)
    topic = models.CharField(blank=True,null=True,max_length=200)
    # task_number = models.CharField(blank = True, null=True,max_length=200)
class UploadTaskFiles(models.Model):
    file = models.FileField(blank=True,upload_to='tasks')
    task_number = models.CharField(blank = True, null=True,max_length=200)

class UploadFiles(models.Model):
    file = models.FileField(blank = True,upload_to = 'homework')
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,)
    task_number = models.IntegerField(blank = True, null=True)
    room_code = models.CharField(max_length=200,blank=True,null=True) 
class Comments(models.Model):
    value = models.CharField(max_length=10000000000)
    date = models.DateTimeField(null=True,blank=True)
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,)
    room = models.CharField(max_length=200,blank=True,null=True)
    task_id=models.IntegerField(blank=True, null=True)

class Topic(models.Model):
    name = models.CharField(blank=True, max_length=100)
    room = models.CharField(max_length=200,blank=True,null=True)
    author = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,)

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio =models.TextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to='test/')
    github_url=models.CharField(max_length=255,null=True)
    facebook_url=models.CharField(max_length=255,null=True)
    instagram_url=models.CharField(max_length=255,null=True)
    
    
    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("home")

class Mark(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE,)
    classroom_code = models.CharField(max_length=200)
    classroom_name = models.CharField(max_length=200)
    mark = models.FloatField()
    task_number = models.CharField(blank = True, null=True,max_length=200)

    
