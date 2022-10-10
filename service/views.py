from re import template
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
# HttpResponseRedirect, HttpResponseNotFound, StreamingHttpResponse
from django.urls import reverse
from django.template.loader import get_template
from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist

from .models import Product

def index(request):
    #template = get_template('index.html')
    return render(request, 'index.html')
    #return HttpResponse(template.render())
    #cont = ('hello', ' world')
    #resp = HttpResponse(cont)
    #resp = StreamingHttpResponse(cont)
    #return resp
    # return HttpResponse('Hello World')

def page(request, page_num):
    return HttpResponse(f'Page {page_num}')

def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404('NOT Found')
        # return HttpResponseNotFound('NOT Found')
        # raise HttpResponseNotFound('NOT Found')
    return HttpResponse('OK')
    # return HttpResponseRedirect(reverse('service'))
    # res = HttpResponse('Hello World')
    # return HttpResponseRedirect('service')
    # return HttpResponse(f'{res.content}')
    # return HttpResponse(f'{request.method}')
    # return HttpResponse(f'{request.scheme}')
    # a = int(request.GET.get('a'))
    # b = int(request.GET.get('b'))
    # c = a + b
    # return HttpResponse(f'{c}')
    # return HttpResponse(f'{request.headers}')
    # return HttpResponse(f'{dict(request.GET)}')
    # return HttpResponse(f'{res.status_code}')
    
#def file_show(req):
 #   file = 'service/pictures1.jpg'
  #  return FileResponse(open(file, 'rb'), as_attachment=True, filename='home')
def json_show(req):
    data = {'cost':12, 'title':'book'}
    return JsonResponse(data)