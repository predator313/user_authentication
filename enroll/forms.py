from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
#here we are going to add some more lebels to ours forms
class Sign_Upform(UserCreationForm):
    password2=forms.CharField(label='Conform Password(Again)',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

#now let little bit customise the userchangeform
#like usercreation form we need to customise here also
class Editform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class EditAdminform(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'
        #since this is admin so admin has right to acces all details
        #normal user has limited right to use