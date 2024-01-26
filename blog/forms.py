from django import forms
from .models import Blog


# class BlogForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     body = forms.CharField()
#     author = forms.ChoiceField()


class BlogForm(forms.ModelForm):
    title = forms.CharField(label='موضوع خبر')
    body = forms.CharField(widget=forms.Textarea(), label='متن خبر')

    class Meta:
        model = Blog
        fields = '__all__'
