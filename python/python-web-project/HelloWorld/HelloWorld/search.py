from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
def  search_form(request):
	return render_to_response('search_form.html')

def  search(request):
	request.encoding='utf-8'
	if  'q' in request.GET:
		message = '你搜索的内容为：'+ request.GET['q']
	else:
		message ='你提交了空表单'
	return HttpResponse(message)