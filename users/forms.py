from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, JProfile


class UserRegisterForm(UserCreationForm):
    password1 = forms.Field(widget=forms.PasswordInput(attrs={'class':'register-form__input','placeholder': '8자리이상 숫자+문자로 구성해주세요.'}))
    password2 = forms.Field(widget=forms.PasswordInput(attrs={'class':'register-form__input','placeholder': '이전과 동일한 비밀번호를 입력하세요.'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
                'username': forms.TextInput(attrs={
                    'class':'register-form__input',
                    'placeholder': '15자 이내로 입력하세요.',
                    'maxlength':20, 'autofocus': True,
                    'required':'required'})
            }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'dream', 'hobby', 'interest']
        widgets = {
                'nickname': forms.TextInput(attrs={
                    'class':'register-form__input',
                    'placeholder': '수정이 불가능하니 신중하게 입력해주세요.',
                    'maxlength':10}),
                'dream': forms.TextInput(attrs={
                    'class':'register-form__input',
                    'placeholder': '소중한 꿈 한 개만 입력하세요.',
                    'maxlength':10}),
                'hobby': forms.TextInput(attrs={
                    'class':'register-form__input',
                    'placeholder': '취미를 입력하세요.',
                    'maxlength':10}),
                'interest': forms.TextInput(attrs={
                    'class':'register-form__input',
                    'placeholder': '최근 관심사를 입력하세요.',
                    'maxlength':20}),
            }


class JProfileForm(forms.ModelForm):
    class Meta:
        model = JProfile
        fields = ['political_orientation']
        widgets = {'political_orientation': forms.RadioSelect(),'required':'required'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['political_orientation'].widget.choices.pop(0)



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'dream', 'hobby', 'interest']

        widgets = {
                'dream': forms.TextInput(attrs={
                    'class':'profile_update-form__input',
                    'maxlength':10}),
                'hobby': forms.TextInput(attrs={
                    'class':'profile_update-form__input',
                    'maxlength':10}),
                'interest': forms.TextInput(attrs={
                    'class':'profile_update-form__input',
                    'maxlength':20}),
            }


class JProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = JProfile
        fields = ['department', 'political_orientation']
        widgets = {'department': forms.RadioSelect(),'required':'required',
                   'political_orientation': forms.RadioSelect(),'required':'required'
                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].widget.choices.pop(0)
        self.fields['political_orientation'].widget.choices.pop(0)



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
