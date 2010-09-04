from datetime import date
import os
from pyPdf import PdfFileWriter, PdfFileReader

def is_valid_pdf(filepath):
	'''Validates that file is proper PDF-File'''
	try:
		from pyPdf import PdfFileReader
		from pyPdf.utils import PdfReadError
		PdfFileReader(open(filepath, "rb"))
	except PdfReadError:
		return False
	return True
