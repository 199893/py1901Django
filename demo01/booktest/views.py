from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo
from django.template import loader

# Create your views here.

def index(request):
    # # print('请求',request)
    # # return HttpResponse('首页')
    # #加载模板
    # indextem=loader.get_template('booktest/index.html')
    # cont={'username':'jmx'}
    # #使用变量参数渲染模板
    # result=indextem.render(cont)
    # # 返回模板
    # return HttpResponse(result)

    #简写方法

    # cont={'username':'jmx'}
    return render(request,'booktest/index.html',{'username':'jmx'})

def list(request):
    # print('请求',request)
    # return HttpResponse('list')
    booklist=BookInfo.objects.all()
    cont={'booklist':booklist}
    return render(request,'booktest/list.html',cont)

def detail(request,id):
    # return HttpResponse('123')
    # try:
    #     book=BookInfo.objects.get(pk=int(id))
    #     return HttpResponse(book)
    # except:
    #     return HttpResponse('请输入正确id')
    book=BookInfo.objects.get(pk=id)
    # cont={'book':book}
    return render(request,'booktest/detail.html',{'book':book})

def delete(request,id):
    try:
        BookInfo.objects.get(pk=id).delete()
        booklist = BookInfo.objects.all()
        return render(request, 'booktest/list.html', {'booklist': booklist})
    except:
        return HttpResponse('删除失败')

def addhero(request):

    return  render(request,'booktest/addhero.html',)


'''
视图函数 
将函数和路由绑定
'''