from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404
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