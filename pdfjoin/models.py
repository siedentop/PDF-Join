from django.db import models
from django import forms
import datetime

class FileGroup(models.Model):
	'''
	A collection of files that are to be merged. 
	'''
	filename = models.CharField('Filename', max_length=100, help_text='Name of the output')
	title = models.CharField('Title', max_length=100, help_text='Title of the generated PDF', blank = True, null=True)
	author = models.CharField('Author', max_length=100, help_text="Author's Name", blank= True)
	datetime = models.DateTimeField('Time and Day', default=datetime.datetime.now())
	file = forms.FileField()
	
	def __unicode__(self):
		return self.filename

class PdfFile(models.Model):
	''' The PDF-File to be merged. '''
	filegroup = models.ForeignKey(FileGroup)
	file = models.FileField(upload_to='uploads')
	
class FileGroupForm(forms.Form):
	filename = forms.CharField(label='Filename', max_length=100)
	title = forms.CharField(label='Title', max_length=100, required=False)
	author = forms.CharField(label="Author", max_length=100, required=False)
	datetime = forms.DateTimeField(widget=forms.DateTimeInput(), initial=datetime.datetime.now())
	file1 = forms.FileField(label="File 1", required=True)
	
	def save(self):
		new_filegroup = FileGroup.objects.create(filename=self.cleaned_data['filename'], 
		                                         title= self.cleaned_data['title'], 
		                                         author = self.cleaned_data['author'], 
		                                         datetime = self.cleaned_data['datetime'],)
		if not self.is_valid():
			raise ValueError("Form was not filled corretly.")
		return new_filegroup

