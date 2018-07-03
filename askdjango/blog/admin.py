#blog/admin.py
from django.contrib import admin
from .models import Post, Comment
#1.9부터 태그를 표현하는 방법
from django.utils.safestring import mark_safe
#기본적으로 태그를 escape 해준다 장고는 즉 위의 함수를 임포트 하여 허용해야한다
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size','status', 'created_at', 'updated_at']
    actions = ['make_published', 'make_draft', 'make_withdrawn']

    def content_size(self, post):
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content)))
    content_size.short_description = '내용 글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p') #QuerySet.update
        #자동으로 카운트 되는건가 ?
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count)) #django 메세지 프레임워크 활용
    make_published.short_description = '지정 포스팅을 Published상태로 변경합니다'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d') #QuerySet.update
        #자동으로 카운트 되는건가 ?
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count)) #django 메세지 프레임워크 활용
    make_draft.short_description = '지정 포스팅을 Draft상태로 변경합니다'

    def make_withdrawn(self, request, queryset):
        updated_count = queryset.update(status='w') #QuerySet.update
        #자동으로 카운트 되는건가 ?
        self.message_user(request, '{}건의 포스팅을 Withdrawn상태로 변경'.format(updated_count)) #django 메세지 프레임워크 활용
    make_withdrawn.short_description = '지정 포스팅을 Withdrawn상태로 변경합니다'

    #위의 묘사를 다르게해줌 모델에서 지정한 verbose_name = '제목' 와 같이
    #content_size.allow_tags = True
    #1.9 부터 삭제 1.9부터는 django mark_safe라는 함수를 이용
    # 컨텐츠 사이즈 리스트에 태그를 허용함을 의미
# Register your models here.
#어드민에 모델을 등록하는 과정
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    pass