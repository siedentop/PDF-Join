from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf

from pdfjoin.forms import *

from pyPdf import PdfFileReader, PdfFileWriter
from pyPdf.utils import PdfReadError

#@csrf_protect
def show_start(request):
	'''Shows a start page for PDF-Join. '''
	if request.method == 'POST':
		form = FileGroupForm(request.POST, request.FILES)
		if form.is_valid():
			
			errors = []
			import StringIO
			output = PdfFileWriter()
			for name in request.FILES:
				upload = request.FILES[name]
				infile = StringIO.StringIO()
				infile.write(upload.read())
				try:
					pdf = PdfFileReader(infile)
				except PdfReadError: 
					errors.append("Error with your file '%s.' " % upload.name)
					continue
				for page in pdf.pages:
					output.addPage(page)
					
			if len(errors) != 0:
				return render_to_response('pdfjoin/start.html', {'form': form,  'errors':errors}, context_instance=RequestContext(request))

			# Set filename
			filename = request.POST['title']
			filename = filename.split('.')[0] + '.pdf'
			
			response = HttpResponse(mimetype="application/pdf")
			response['Content-Disposition'] = 'attachment; filename=%s' % filename
			
			output.write(response)
			infile.close()
			return response
	else:
		form = FileGroupForm()
	return render_to_response('pdfjoin/start.html', {'form': form }, context_instance=RequestContext(request))


def csrf_failure(request, reason=""):
	return render_to_response('403.html')
	