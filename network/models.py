from django.db import models

# Create your models here.

class  Video(models.Model):
	mid=models.IntegerField(default=0)	
	url=models.CharField(max_length=256,default="")
	stage=models.CharField(max_length=128,default="")
	subj=models.CharField(max_length=128,default="")
	name=models.CharField(max_length=128,unique=True)

class  Articles(models.Model):
	mid=models.IntegerField(default=0)	
	title=models.CharField(max_length=256,default="")
	subj=models.CharField(max_length=128,default="")
	content=models.CharField(max_length=128,default="")
	readcount=models.IntegerField(default=0)
	goodcount=models.IntegerField(default=0)	
	comment=models.CharField(max_length=256,default="")

class  Questions(models.Model):
	mid=models.IntegerField(default=0)	
	title=models.CharField(max_length=256,default="")
	subj=models.CharField(max_length=128,default="")
	##jibie?
	stage=models.CharField(max_length=128,default="")
	content=models.CharField(max_length=1280,default="")
	answers=models.CharField(max_length=128,default="")

class  PersonInfo(models.Model):
	mid=models.IntegerField(default=0)	
	mstunum=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	sex=models.CharField(max_length=128,default="")
	school=models.CharField(max_length=128,default="")
	grade=models.IntegerField(default=0)	
	age=models.IntegerField(default=0)	

class  UserInfo(models.Model):
	mid=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	passwd=models.CharField(max_length=128,default="")
	liimit=models.CharField(max_length=128,default="")

class  Score(models.Model):
	mid=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	subj=models.CharField(max_length=128,default="")
	score=models.IntegerField(default=0)
	testdate=models.DateField()
	rand=models.IntegerField(default=0)	
	level=models.CharField(max_length=128,default="")

class  Comment(models.Model):
	mid=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	commentdate=models.DateField()
	commentcontent=models.CharField(max_length=1280,default="")

class  History(models.Model):
	mid=models.IntegerField(default=0)	
	name=models.CharField(max_length=128,default="")
	article=models.CharField(max_length=128,default="")
	video=models.CharField(max_length=128,default="")