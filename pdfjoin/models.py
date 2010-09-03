from django.db import models

class FileGroup(models.Model):
	'''
	A collection of files that are to be merged. 
	'''
	filename = models.CharField('Filename', max_length=100, help_text='Name of the output')
	title = models.CharField('Title', max_length=100, help_text='Title of the generated PDF', blank = True)
	author = models.CharField('Author', max_length=100, help_text="Author's Name", blank= True)
	datetime = models.DateTimeField('Time and Day') #TODO: make default = now
	
	def __unicode__(self):
		return self.filename

class PdfFile(models.Model):
	''' The PDF-File to be merged. '''
	filegroup = models.ForeignKey(FileGroup)
	file = models.FileField(upload_to='uploads')
	
#todo atleast one pdffile required...