from datetime import date
import os
from pyPdf import PdfFileWriter, PdfFileReader

MEDIA_ROOT = "/home/chris/devel/toolsite/media/"
UPLOAD_PATH = 'uploads/'

def handle_uploads(FILES):
	''' Function to handle upload of files '''
	saved = []
	
	upload_dir = date.today().strftime(UPLOAD_PATH)
	upload_full_path = os.path.join(MEDIA_ROOT, upload_dir)

	if not os.path.exists(upload_full_path):
		os.makedirs(upload_full_path)

	for key in FILES:
		upload = FILES[key]
		while os.path.exists(os.path.join(upload_full_path, upload.name)):
			upload.name = '_' + upload.name
		dest = open(os.path.join(upload_full_path, upload.name), 'wb')
		for chunk in upload.chunks():
			dest.write(chunk)
		dest.close()
		saved.append(os.path.join(upload_dir, upload.name))
	# returns [(key1, path1), (key2, path2), ...]
	return saved
	
def generate_pdf(files):
	output = PdfFileWriter()
	for f in files:
		print f, files[f]
		pdf = PdfFileReader(open(f.__str__(), 'rb'))
		for page in pdf.pages:
			output.addPage(page)
	outfile = open("output.pdf", "wb")
	output.write(outfile)
	outfile.close()
	return outfile

def is_valid_pdf(filepath):
	'''Validates that file is proper PDF-File'''
	try:
		from pyPdf import PdfFileReader
		from pyPdf.utils import PdfReadError
		PdfFileReader(open(filepath, "rb"))
	except PdfReadError:
		return False
	return True
