from django.contrib import admin
from .models import Booktest,Borrows,Stunden,HotPic,HeroInfo
# Register your models here.
admin.site.register(Borrows)
admin.site.register(Booktest)
admin.site.register(Stunden)
admin.site.register(HotPic)
admin.site.register(HeroInfo)