from django.contrib import admin
from .models import Booktest,Borrows,Stunden
# Register your models here.
admin.site.register(Borrows)
admin.site.register(Booktest)
admin.site.register(Stunden)