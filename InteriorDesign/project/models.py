from django.db import models
from django.urls import reverse

class Project(models.Model):
	title = models.CharField(max_length=50)
	TYPE = (
		('Office', 'Office'),
		('Residential', 'Residential'),
		('Commercial', 'Commercial')
	)
	type =models.CharField(max_length=50, null= True, choices= TYPE)
	description = models.CharField(max_length=220)
	image = models.ImageField(upload_to='images')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('project:project_detail', kwargs={
			'project_id': self.id
        })