from django.conf.urls import url
from . import views

app_name='booktest'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^list/$', views.list,name='list'),
    url(r'^detail/(\d+)/$', views.detail),
    url(r'delete/(\d+)/$',views.delete),
    url(r'^addbook/$',views.addbook),
    url(r'^addbookhandler/$',views.addbookhandler),
    url(r'^addhero/(\d+)/$',views.addhero),
    url(r'^addherohandler/$',views.addherohandler),
    url(r'^deletehero/(\d+)/$',views.deletehero),
    url(r'^area/$',views.area),
    url(r'^login/$',views.login,name='login'),
]