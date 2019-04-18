from django.contrib import admin
from .models import issueInfo,answerInfo
# Register your models here.

class answerInfoInline(admin.StackedInline):
    model = answerInfo
    extra = 1

class issueInfoAdmin(admin.ModelAdmin):
    list_filter = ['isname']

    inlines = [answerInfoInline]

class answerInfoAdmin(admin.ModelAdmin):
    list_filter = ['awname']

admin.site.register(issueInfo,issueInfoAdmin)
admin.site.register(answerInfo,answerInfoAdmin)
