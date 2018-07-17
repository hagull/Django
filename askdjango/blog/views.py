from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.http import Http404
from .forms import PostForm
# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains = q)
    return render(request, 'blog/post_list.html', {
        'post_list' : qs,
        'q' :q,
    })
def post_detail(request, id):
#try:
#   post = Post.objects.get(id=id)
#    except Post.DoesNotExist:
#        raise Http404 # 이렇게 처리해야함 근데 많이 번거로움
    #그래서 위와 같은 코드인
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html',{
        #'post_title' : post.title,
        #'post_author' : post.author,
        #'post_content' : post.content,
        'post' : post,#템플릿에 post가 넘겨진다
    })
def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            #post.user = request.user
            #post.save()
            return redirect(post) # post.get_absolute_url() => post detail view
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form
    })
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid(): # 유효성 검사가 수행됨
            post = form.save()
            #post.user = request.user
            #post.save()
            return redirect(post) # post.get_absolute_url() => post detail view
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form
    })

def post_test(request):
    return render(request, 'blog/post_test.html')