from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'detail/(\d+)/$',views.detail),
    # url(r'delete/(\d+)/$',views.delete),
    url(r'details/$',views.details),
    url(r'da/(\d+)/$',views.da),
]