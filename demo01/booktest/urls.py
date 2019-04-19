from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^list/$', views.list),
    url(r'^detail/(\d+)/$', views.detail),
    url(r'delete/(\d+)/$',views.delete),
    url(r'^addhero/(\d+)/$',views.addhero),
]