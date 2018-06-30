#blog/model.py
from django.db import models
import re
from django.forms import ValidationError
from django.utils import timezone

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    author = models.CharField(max_length=20)
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
# Create your models here.
    def __str__(self):
        return self.title