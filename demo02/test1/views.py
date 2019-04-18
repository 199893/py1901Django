from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import issueInfo,answerInfo
# Create your views here.

def index(request):
    # return HttpResponse('111111')
    ls=issueInfo.objects.all()
    return render(request,'test1/index.html',{'ls':ls})

def detail(request,id):
    lsid=issueInfo.objects.get(pk=id)
    return render(request,'test1/detail.html',{'lsid':lsid})

def details(request):
    # wer=answerInfo.ge

    res=request.GET['votenum']
    asd=answerInfo.objects.get(pk=res)
    asd.votes=int(asd.votes)
    asd.votes+=1
    asd.save()
    print(asd.votes)
    ewq = asd.isnameid_id
    print(ewq)
    # return HttpResponse('11111')
    return HttpResponseRedirect('/test1/da/'+str(ewq)+'/')

def da(request,id):
    res = answerInfo.objects.all()
    # return HttpResponse('111111')
    return render(request,'test1/details.html',{'res':res})

# def delete(request,id):
#     try:
#         issueInfo.objects.get(pk=id).delete()
#         isslist = issueInfo.objects.all()
#         return render(request, 'booktest/list.html', {'isslist': isslist})
#     except:
#         return HttpResponse('删除失败')
