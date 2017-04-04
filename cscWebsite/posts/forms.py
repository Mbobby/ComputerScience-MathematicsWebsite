from django import forms
from models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
	post_body = forms.CharField(widget=TinyMCE(attrs={'cols': 60, 'rows': 30}))
	class Meta:
		model = Post
		fields = ('post_title', 'post_body', 'post_preview')