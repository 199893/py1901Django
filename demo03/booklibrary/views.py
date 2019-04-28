from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Booktest,Borrows,Stunden
# Create your views here.

#首页
def index(request):
    return render(request,'booklibrary/index.html')

#用户登录
def login(request):
    user=Stunden.objects.all()

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        for i in user:
            if username==i.username and password==i.password:
                request.session['username']=username
                return redirect(reverse('book:reader'))
                # return HttpResponse('成功')
        return HttpResponse('账号或密码不正确')
    else:
        return render(request, 'booklibrary/reader_login.html')


#注册用户
def register(request):
    user = Stunden()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        college=request.POST['college']
        sno=request.POST['number']
        eml=request.POST['email']

        if password==password2:
            user.username=username
            user.password=password
            user.college=college
            user.sno=sno
            user.eml=eml
            user.save()
            return redirect(reverse('book:login'))
        else:
            return HttpResponse('两次密码不一致')

    else:
        return render(request, 'booklibrary/register.html')

#登录成功界面
def reader(request):
    username=request.session.get('username',None)
    return render(request,'booklibrary/reader.html',{'username':username})

#个人信息
def info(request):
    username=request.session.get('username')
    user = Stunden.objects.get(username=username)
    return render(request,'booklibrary/info.html',{'user':user})

#修改
def modify(request):
    username = request.session.get('username')
    user = Stunden.objects.get(username=username)

    if request.method=='POST':
        #获取post
        username = request.POST['username']
        password = request.POST['password']
        college = request.POST['college']
        sno = request.POST['number']
        eml = request.POST['email']
        # print(username,password,college,sno,eml)

        #修改
        user.username = username
        user.password=password
        user.college = college
        user.sno = sno
        user.eml = eml
        user.save()
        return redirect(reverse('book:info'))
    else:
        return render(request,'booklibrary/modify.html',{'user':user})


def query(request):

    # return HttpResponse('123')
    return render(request,'booklibrary/query.html')