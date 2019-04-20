from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^list/$', views.list),
    url(r'^detail/(\d+)/$', views.detail),
    url(r'delete/(\d+)/$',views.delete),
    url(r'^addbook/$',views.addbook),
    url(r'^addbookhandler/$',views.addbookhandler),
    url(r'^addhero/(\d+)/$',views.addhero),
    url(r'^addherohandler/$',views.addherohandler)
]