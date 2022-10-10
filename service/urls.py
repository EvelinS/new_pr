from django.urls import path, re_path #, register_converter
from service.views import index, page, about, json_show #file_show 
# from service import converts

# register_converter(converts.CheckParam, "dif_type") 

urlpatterns = [
    # path('service/', index, name='service'),
    path('', index, name='service'),
    re_path(r'^service/(?P<page_num>[0-9]{3})/$', page),
    # path('service/<dif_type:page_num>', page)
    path('about/<int:id>', about, name='about'),
    # path('file', file_show, name='file_show')
    path('json', json_show, name='json_show'),
]