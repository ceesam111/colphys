from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_users.models import UserProfileInfo

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

        # widgets = {
        # "password":"forms.PasswordInput()",
        # }

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    HOC_code = forms.CharField(required=True)
    matric_no = forms.CharField(required=True)
    bio = forms.CharField(required=False)
    HOC = 'HOC'
    student = 'student'
    parent = 'parent'
    user_types = [
        (student, 'student'),
        (parent, 'parent'),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = UserProfileInfo
        fields = ( 'HOC_code', 'matric_no', 'bio', 'profile_pic', 'user_type')
