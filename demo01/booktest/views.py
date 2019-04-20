from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import BookInfo,HeroInfo
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

def addbook(request):
    # return HttpResponse('123')
    return render(request,'booktest/addbook.html',{})

def addbookhandler(request):
    btitle=request.POST['btitle']
    # print(btitle)

    b=BookInfo()
    b.btitle=btitle
    b.save()

    # return HttpResponse('456')
    return HttpResponseRedirect('/booktest/list/')

def delete(request,id):
    try:
        BookInfo.objects.get(pk=id).delete()
        booklist = BookInfo.objects.all()
        return HttpResponseRedirect('/booktest/list', {'booklist': booklist})
    except:
        return HttpResponse('删除失败')

def addhero(request,bookid):

    return render(request,'booktest/addhero.html',{'bookid':bookid})

def addherohandler(request):
    bookid=request.POST['bookid']
    hname=request.POST['heroname']
    hgcnder=request.POST['sex']
    hcontent=request.POST['herocontent']
    # print(bookid,hname,hgcnder,hcontent)

    book=BookInfo.objects.get(pk=bookid)
    hero=HeroInfo()
    hero.hname=hname
    hero.hgender=True
    hero.hcontent=hcontent
    hero.hBook=book
    hero.save()


    return HttpResponseRedirect('/booktest/detail/'+str(bookid)+'/',{'book':book})
    # return HttpResponse('123')

'''
视图函数 
将函数和路由绑定
'''