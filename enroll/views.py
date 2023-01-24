from django.shortcuts import render

# Create your views here.
from . forms import Sign_Upform,Editform,EditAdminform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm #this inbuilt form is for authentication
#we use userchangeform through Editfrom 
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect

# Create your views here.
#usig user creation forms we get three default filed
#username ,password and passwordconfimations
def Sign_Up(request):
    #the inbuilt user creation form is successfully rendered and this is full authenticated
    #we need only few modification here
    #we should make ours practice to use the post request concept
    #since we are going to save data
    if(request.method=='POST'):
        fm=Sign_Upform(request.POST)
        if(fm.is_valid()):
            fm.save()
            messages.success(request,'hey your account is created successfully')
           
    else:
        fm=Sign_Upform()
    return render(request,'enroll/signup.html',{'form':fm})

#now lets create the login form
def Log_in(request):
    if not request.user.is_authenticated: #if user is
        #already login then should not do the log in again
        #we simply redrict the user to the profile page so we use this
        #not request.user.is_authenticated concept
        if(request.method=="POST"):
            fm=AuthenticationForm(request=request,data=request.POST)
            if(fm.is_valid()):
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(request,username=uname,password=upass)
                if user:
                    login(request,user)
                    messages.success(request,'hey you logged in successfully')
                    return HttpResponseRedirect('/dashb/')
                
                
        else:
            fm=AuthenticationForm()
        return render(request,'enroll/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashb/')

#log out section using inbuilt log out features
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/dashb/')

#using profile or dashboard features of the django.contrib.auth
def dashboard(request):
    if request.user.is_authenticated:
        pass
    else:
        return HttpResponseRedirect('/login/')
