
#blog/views_cbv.py
from django.views.generic import CreateView
from .models import Post
from django import forms
#원래 blog/forms.py에 구현
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreatView(CreateView):
    model = Post
    form_class = PostForm
    #success_url = '/'
post_new = PostCreatView.as_view()