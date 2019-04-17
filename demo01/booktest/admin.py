from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.

class HeroInfoInline(admin.StackedInline):
    '''关联'''
    model = HeroInfo
    #关联数
    extra = 1

class HeroInfoAdmin(admin.ModelAdmin):
    #排序显示
    list_display = ['hname','hgender','hBook']
    #右侧显示过滤框
    list_filter = ['hname']
    #查询框
    search_fields = ['hname']
    #分页
    list_per_page = 3

class BookInfoAdmin(admin.ModelAdmin):
    # 排序显示
    list_display = ['btitle', 'bpub_date']
    # 右侧显示过滤框
    list_filter = ['btitle']
    # 查询框
    search_fields = ['btitle']
    # 分页
    list_per_page = 3

    #关联，添加书时可添加英雄信息
    inlines = [HeroInfoInline]



admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)


'''
通过少量代码实现强大的后台管理
'''