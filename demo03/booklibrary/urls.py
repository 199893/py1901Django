from django.conf.urls import url
from . import views

app_name='book'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^reader/$',views.reader,name='reader'),
    url(r'^info/$',views.info,name='info'),
    url(r'^modify/$',views.modify,name='modify'),
    url(r'^query/$',views.query,name='query'),
]