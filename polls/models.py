from django.db import models

class Poll(models.Model):
	question = models.CharField(max_lenght=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegeField(default=0)
	

# Create your models here.
