# dojo/forms.py

from django import forms

#함수를 만들어 유효성검사를 한다
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')

class PostForm(forms.Form):
    title = forms.CharField(validators= [min_length_3_validator])
    content = forms.CharField(widget = forms.Textarea)
    #모델은 데이터베이스 상의 문자열을 지정해줌
    #폼은 이를 구별하지 않으므로 둘다 CharField가 된다
    #위젯 생성
