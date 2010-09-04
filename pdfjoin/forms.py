from django import forms
import datetime
	
class FileGroupForm(forms.Form):
	''' Form to upload multiple PDF-Files '''
	title = forms.CharField(label='Title', max_length=30, required=True)
	file1 = forms.FileField(label="File 1", required=True)
	file2 = forms.FileField(label="File 2", required=False)
	file3 = forms.FileField(label="File 3", required=False)
	
	def save(self):
		pass
