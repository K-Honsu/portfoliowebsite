from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

# NB: DIFFERENCE BETWEEN NULL AND BLANK FIELD
# NULL MEANS IN THE DATABASE,THE FIELD/TABLE CANNOT BE BLANK
# BLANK MEANS WHEN SUBMITTING THE FORM, WE CAN LET THE FORM BE SUBMITTED WITH NO VALUE
# I.E WHEN SUBMITTING A FORM A POST REQUEST,IT CANNOT BE BLANK
# ForeignKey -> many to one relation i.e a comment can applied single project but a project can have many comment

class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextUploadingField(blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.body[0:50]
    

class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, default='default--skill--icon.png')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.title
    
    
class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    subject = models.CharField(max_length=200,null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.name
    
    
class Endorsement(models.Model):
    name = models.CharField(max_length=200,null=True)
    body = models.TextField() 
    approved = models.BooleanField(default=False, null=True)
    featured = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.body[0:50]
    
