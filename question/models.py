from django.db import models

# Create your models here.

class Inquirer(models.Model):
	title=models.CharField(max_length=255,default='',editable=True)
	date_start=models.DateTimeField()
	date_finish=models.DateTimeField()
	description=models.TextField(default='',editable=True)
	class ReadonlyMeta:
		readonly = ["date_start"]
       

class Questions(models.Model):
	TEXT=1
	ONE_VAR=2
	MANY_SELECT_VAR=3
	QUESTION_ANS_TYPE_CHOICES=(
		(TEXT,'Text'),
		(ONE_VAR,'Choise of option'),
		(MANY_SELECT_VAR,'Many choice'),
	)
	name=models.CharField(max_length=255,null=False)
	type=models.IntegerField(choices=QUESTION_ANS_TYPE_CHOICES,default=TEXT)
	inquirer=models.ForeignKey(Inquirer,on_delete=models.CASCADE,default=None)

class Answers(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=255,null=False)
	questions=models.ForeignKey('Questions',on_delete=models.CASCADE)

class Users(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=255,default='Anonim')

class UserAnswers(models.Model):
	user=models.ForeignKey('Users',on_delete=models.CASCADE)
	answer=models.ForeignKey('Answers',on_delete=models.CASCADE)

class UserInquirer(models.Model):
    user = models.ForeignKey('Users',on_delete=models.CASCADE)
    inquirer = models.ForeignKey('Inquirer',on_delete=models.CASCADE)
