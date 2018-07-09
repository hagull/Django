#dojo/view.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404
from .models import Post

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
def post_list1(request):
    name = '남태식'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 장고 어쩌구</p>
    '''.format(name=name))
def post_list2(request):
    name = '남태식'
    return render(request, 'dojo/post_list.html', {'name' : name})
def post_list3(request):
    return JsonResponse({
        'message' : '안녕 파이썬 &장고',
        'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params = {'ensure_ascii' : False})
# message와 item을 json 형태로 반환해줌
def excel_download(request):
    #filepath = '/Users/NamTaeSik/Django/askdjango/dojo/other/path/excel.xls'
    filepath = os.path.join(settings.BASE_DIR, 'excel.xls')
    filename = os.path.basename(filepath)
    #BASE_DIR는 최상위 디렉토리의 값이 있다.(프로젝트 최상위디렉토리 askdjango)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
#form 메소드
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # forms.py의 클래스 지정
        if form.is_valid():
            # 방법1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            #방법 2
            # post = Post(title = form.cleaned_data['title'],
            #             content = form.cleaned_data['content'])
            # post.save()

            # 방법 3
            # post = Post.objects.create(title=form.cleaned_data['title'],
            #                            content = form.cleaned_data['content'])

            # 방법 4
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            # post = Post.objects.create(**form.cleaned_data)
            post.save()
            print(form.cleaned_data)
            return redirect('/dojo/') # namespace:name 을 사용할수도있음
        pass
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
        'form' : form,
    })
def post_edit(request,id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        # forms.py의 클래스 지정
        if form.is_valid():
            # 방법1
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            #방법 2
            # post = Post(title = form.cleaned_data['title'],
            #             content = form.cleaned_data['content'])
            # post.save()

            # 방법 3
            # post = Post.objects.create(title=form.cleaned_data['title'],
            #                            content = form.cleaned_data['content'])

            # 방법 4
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            # post = Post.objects.create(**form.cleaned_data)
            post.save()
            print(form.cleaned_data)
            return redirect('/dojo/') # namespace:name 을 사용할수도있음

    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
        'form' : form,
    })
#수정기능 구현
