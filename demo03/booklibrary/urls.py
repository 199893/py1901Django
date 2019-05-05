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
    url(r'^book/(\d+)/$',views.book,name='book'),
    url(r'^histroy/$',views.histroy,name='histroy'),


    url(r'^upload/$',views.upload,name='upload'),
    url(r'^text/$',views.text,name='text'),
    url(r'^edit/$',views.edit,name='edit'),
    url(r'^eml/$',views.eml,name='eml'),
    url(r'^active/(.*?)/$',views.active,name='active'),

    url(r'^ajax/$',views.ajax,name='ajax'),
    url(r'^ajaxajax/$',views.ajaxajax,name='ajaxajax'),

    url(r'^ajaxlogin/$',views.ajaxlogin,name='ajaxlogin'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^verifys/$',views.verifys,name='verifys'),

]