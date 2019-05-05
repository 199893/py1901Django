from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import Booktest,Borrows,Stunden,HotPic,HeroInfo
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired
from PIL import  Image,ImageDraw,ImageFont
import random,io
from django.views.decorators.cache import cache_page
# Create your views here.

#首页
# @cache_page(60*15)
def index(request):
    host=HotPic.objects.all()
    return render(request,'booklibrary/index.html',{'host':host})

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

        try:
            if Stunden.objects.get(username=username):
                return HttpResponse('账号已存在')
        except Exception:
            # return HttpResponse('请把信息填写完')
            if password==password2:
                user.username=username
                user.password=password
                user.college=college
                user.sno=sno
                user.eml=eml
                user.state=False
                user.save()

                id = Stunden.objects.get(username=username).id

                serutil=Serializer(settings.SECRET_KEY,50)
                resultid=serutil.dumps({'userid':id}).decode('utf-8')


                send_mail('Django邮件', "<a href='http://127.0.0.1:8000/booklibrary/active/%s'>注册成功点我激活</a>"%(resultid,), settings.DEFAULT_FROM_EMAIL,
                          [eml])
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


#查询书
def query(request):
    if request.method=='POST':
        name=request.POST['query']
        item=request.POST['item']
        if item=='name':
            n=Booktest.objects.filter(bname__contains=name)
            print(n)
            return render(request,'booklibrary/query.html',{'book':n})
        else:
            a=Booktest.objects.filter(author__contains=name)
            print(a)
            return render(request, 'booklibrary/query.html', {'book': a})
    else:
        return render(request,'booklibrary/query.html')

#查看书信息
def book(request,id):
    borr=Borrows()
    name=request.session.get('username',None)
    boor = Borrows.objects.filter(name=name)[0]
    book=Booktest.objects.get(pk=id)
    if request.method=='POST':
        borr.book_id=book
        borr.author=User.objects.get(pk=1)
        borr.name=request.session.get('username', None)
        borr.save()

        return redirect(reverse('book:book',args=(id,)),{'boor':boor})

    else:
        time=datetime.now()+timedelta(days=30)
        return render(request,'booklibrary/book.html',{'book':book,'boor':boor,'time':time})


#查看借阅
def histroy(request):
    name = request.session.get('username', None)
    histroys=Borrows.objects.filter(name=name).all()
    # print(histroys[0].)
    # pr=Booktest.objects.get(pk=histroys[0].book_id)
    return render(request,'booklibrary/histroy.html',{'histroys':histroys})

#上传图片
def upload(request):
    if request.method=='GET':
        return render(request,'booklibrary/upload.html')
    elif request.method=='POST':
        # 文件数据需要使用FILES 获取  enctype = "multipart/form-data"
        hp = HotPic()
        hp.name=request.POST['name']
        hp.index=request.POST['index']
        hp.pic=request.FILES['pic']
        hp.save()
        return redirect(reverse('book:index'))

#富文本显示
def text(request):
    text=HeroInfo.objects.all()
    return render(request,'booklibrary/text.html',{'text':text})

#编辑富文本
def edit(request):
    if request.method=='GET':
        return render(request,'booklibrary/edit.html')
    elif request.method=='POST':
        book=HeroInfo()

        book.hcontent=request.POST['hcontent']
        book.hname=request.POST['name']
        book.save()
        return redirect(reverse('book:text'))


def eml(request):
    try:
        send_mail('Django邮件0','Django可以发送邮件',settings.DEFAULT_FROM_EMAIL, ["695205458@qq.com"])
        return HttpResponse('发送成功')
    except Exception:
        return HttpResponse('发送失败')

def active(request,idstr):

    deser=Serializer(settings.SECRET_KEY,50)
    try:
        obj=deser.loads(idstr)
        user=Stunden.objects.get(pk=obj['userid'])
        user.state=True
        user.save()
        return redirect(reverse('book:login'))
    except SignatureExpired as e:
        return HttpResponse('链接已失效')

def ajax(request):
    return render(request,'booklibrary/ajax.html')

def ajaxajax(request):
    text = HeroInfo.objects.all()
    return render(request, 'booklibrary/text.html', {'text': text})



def ajaxlogin(request):
    if request.method=='GET':
        return render(request,'booklibrary/ajaxlogin.html')
    elif request.method=='POST':
        usernmae=request.POST['username']
        password=request.POST['password']
        verifycode=request.POST['verifycode']
        if verifycode==request.session['verifycode']:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('验证码错误')

def verify(request):

    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width=100
    heigth=25

    im=Image.new('RGB',(width,heigth),bgcolor)

    draw=ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('HARNGTON.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')

def verifys(request):
    if request.method=='POST':
        username=request.POST['username']
        if len(Stunden.objects.filter(username=username)):
            return HttpResponse('√')
        else:
            return HttpResponse('×')
