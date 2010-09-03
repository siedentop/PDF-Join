from django.contrib import admin
from pdfjoin.models import *

class FileAdmin(admin.TabularInline):
	model = PdfFile
	

class FileGroupAdmin(admin.ModelAdmin):
	inlines = [
		FileAdmin,
	]

admin.site.register(FileGroup, FileGroupAdmin)
