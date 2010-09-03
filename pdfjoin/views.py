from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from utils import handle_uploads

def show_start(request):
	'''Shows a start page for PDF-Join. '''
	return render_to_response('pdfjoin/start.html')
