from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf

from utils import handle_uploads
from pdfjoin.models import *

#@csrf_protect
def show_start(request):
	'''Shows a start page for PDF-Join. '''
	if request.method == 'POST':
		form = FileGroupForm(request.POST, request.FILES)
		if form.is_valid():
			files = handle_uploads(request.FILES)
			filegroup = form.save()
			output = generate_pdf(files)
			return HttpResponseRedirect('/')
	else:
		form = FileGroupForm()
	return render_to_response('pdfjoin/start.html', {'form': form }, context_instance=RequestContext(request))
