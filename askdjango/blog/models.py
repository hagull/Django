#blog/model.py
from django.db import models
import re
from django.forms import ValidationError
from django.utils import timezone
from django.conf import settings

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name= 'blog_post_set')
    # author = models.CharField(max_length=20)
    #blank 옵션을 주지않으면 필수필드이다
    title = models.CharField(max_length=100, verbose_name = '제목', help_text = '포스팅 제목을 입력해주세요. 최대 100자') # 길이 제한이 있는 문자열
    content = models.TextField(verbose_name= '내용')#길이 제한이 없는 문자열
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                              help_text='위도/경도 포맷으로 입력',
                              validators=[lnglat_validator])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices= STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    #아래 Post와 다르게 문자열로 지정가능 아래는 되고 위는 안되는 이유는 Post가 가장 윗단에서 지정되었기 때문에

    class Meta:
        ordering = ['-id']
        #-붙이면 내림차순
# Create your models here.
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(Post)
    # 이를 통해 post의 id 와 관계시킬수있다. ex ) parent 라고 하면 parent_id라는 columns가 생성
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    #blog_tag_set이란 중간테이블도 생성