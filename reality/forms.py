from django import forms
from .models import Post


class NovelPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        widgets = {
            'title' : forms.TextInput(attrs={'size': '100', 'placeholder':'글자제한은 50자 입니다.'}),
            'contents': forms.Textarea(
                        attrs={
                        'rows': 30,
                        'cols': 140,
                        'placeholder':'글자제한은 1400자 입니다.'
                            }
                        ),

            }

        labels = {
            'title': '제목',
            'contents': '내용',
        }


class PoetryPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        widgets = {
            'title' : forms.TextInput(attrs={'size': '100', 'placeholder':'글자제한은 50자 입니다.'}),
            'contents': forms.Textarea(
                        attrs={
                        'rows': 30,
                        'cols': 140,
                        'placeholder':'글자제한은 1400자 입니다.'
                        }
                    ),
            }

        labels = {
            'title': '제목',
            'contents': '내용',
        }

class LetterPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        widgets = {
            'title' : forms.TextInput(attrs={'size': '100', 'placeholder':'글자제한은 50자 입니다.'}),
            'contents': forms.Textarea(
                        attrs={
                        'rows': 30,
                        'cols': 140,
                        'placeholder':'글자제한은 1400자 입니다.'
                        }
                    ),
            }

        labels = {
            'title': '제목',
            'contents': '내용',
        }
