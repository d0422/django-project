from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method =="POST":
        #request가 POST방식일 경우에 hello_world_input에 있는 내용을 tmp로 가져와라
        tmp=request.POST.get("hello_word_input")
        #HelloWorld모델 변수를 만들어서 text에 tmp를 넣어줌
        new_hello_world=HelloWorld()
        new_hello_world.text=tmp
        #db에 저장
        new_hello_world.save()

        hello_world_list=HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request,'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})