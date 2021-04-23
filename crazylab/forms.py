from django import forms
from .models import Post


class PublicIdeaPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        widgets = {
            'title' : forms.TextInput(attrs={
                    'class':'joseon_post_title_input',
                    'maxlength':50,
                    'placeholder': '글자제한은 50자 입니다.'}),
            'contents': forms.Textarea(
                        attrs={
                        'class':'joseon_post_contents_input',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


class TodayIdeaPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        widgets = {
            'title' : forms.TextInput(attrs={
                    'class':'joseon_post_title_input',
                    'maxlength':50,
                    'placeholder': '글자제한은 50자 입니다.'}),
            'contents': forms.Textarea(
                        attrs={
                        'class':'joseon_post_contents_input',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


class CrazyIdeaPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        widgets = {
            'title' : forms.TextInput(attrs={
                    'class':'joseon_post_title_input',
                    'maxlength':50,
                    'placeholder': '글자제한은 50자 입니다.'}),
            'contents': forms.Textarea(
                        attrs={
                        'class':'joseon_post_contents_input',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


class QuestionIdeaPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        widgets = {
            'title' : forms.TextInput(attrs={
                    'class':'joseon_post_title_input',
                    'maxlength':50,
                    'placeholder': '글자제한은 50자 입니다.'}),
            'contents': forms.Textarea(
                        attrs={
                        'class':'joseon_post_contents_input',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


class IssueIdeaPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        widgets = {
            'title' : forms.TextInput(attrs={
                    'class':'joseon_post_title_input',
                    'maxlength':50,
                    'placeholder': '글자제한은 50자 입니다.'}),
            'contents': forms.Textarea(
                        attrs={
                        'class':'joseon_post_contents_input',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""


class SystemIdeaPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'contents']
        widgets = {
            'title' : forms.TextInput(attrs={
                    'class':'joseon_post_title_input',
                    'maxlength':50,
                    'placeholder': '글자제한은 50자 입니다.'}),
            'contents': forms.Textarea(
                        attrs={
                        'class':'joseon_post_contents_input',
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
