#dojo/view.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mysum(request, numbers):
    #request:httprquest
    #numbers = "1/2/12/123/12312/
    #numbers = "123/123/////122
    #result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    #빈문자열 처리
    # 위코드는
    # split1 = numbers.split("/")
    # for i in range(len(split1)):
    #   result += split1[i]
    #와 같다
    #sum은 변수지정이 안되네 함수명으로 있어서 그런듯
    return HttpResponse(result)
def hello(request, name, age):
    #return HttpResponse("안녕하세요 " + name + "씨 " + "나이는 " + age + "살이시네요.")
    #또 다르게는 아래와 같이 표현가능
    return HttpResponse('안녕하세요. {}씨 나이는 {}살이시네요.'.format(name, age))