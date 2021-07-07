from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth import get_user_model

class UserUpdateForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email','last_name','first_name']
        labels = {
            'last_name' : '姓',
            'first_name' : '名',
        }
