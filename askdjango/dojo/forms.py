# dojo/forms.py

from django import forms
from .models import Post

#함수를 만들어 유효성검사를 한다


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['title', 'content']
    #title = forms.CharField(validators= [min_length_3_validator])
    #content = forms.CharField(widget = forms.Textarea)
    #def save(self, commit = True):
    #    post = Post(**self.cleaned_data)
    #    if commit:
    #        post.save()
    #    return post
    #모델은 데이터베이스 상의 문자열을 지정해줌
    #폼은 이를 구별하지 않으므로 둘다 CharField가 된다
    #위젯 생성
    #폼은 프론트엔드 단에서 입력된 데이터들을 처리해주는 역할 여기서 한것은 추가로 객체로 지정한것을 말한다
    #즉 웹 프론트엔드 단에서의 데이터처리에 도움을 주고 추가로 꾸미는것도 가능