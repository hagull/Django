#blog/admin.py
from django.contrib import admin
from .models import Post
#1.9부터 태그를 표현하는 방법
from django.utils.safestring import mark_safe
#기본적으로 태그를 escape 해준다 장고는 즉 위의 함수를 임포트 하여 허용해야한다
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at']
    def content_size(self, post):
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content)))
    content_size.short_description = '내용 글자수'
    #위의 묘사를 다르게해줌 모델에서 지정한 verbose_name = '제목' 와 같이
    #content_size.allow_tags = True
    #1.9 부터 삭제 1.9부터는 django mark_safe라는 함수를 이용
    # 컨텐츠 사이즈 리스트에 태그를 허용함을 의미
# Register your models here.
