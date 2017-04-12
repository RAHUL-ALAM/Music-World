from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=15,widget = forms.TextInput(attrs=
		{'name':"username",'id':"username",'tabindex':"1",'class':"form-control",'placeholder':"Username"}))
	password = forms.CharField(max_length=15,widget = forms.PasswordInput(attrs=
		{'name':'password','id':'password','tabindex':'2','class':'form-control','placeholder':'Password'}))

class RegisterForm(forms.ModelForm):

	password1 = forms.CharField(widget=forms.PasswordInput(attrs=
		{'name':'password','id':'password','tabindex':'2','class':'form-control','placeholder':'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=
		{'name':'confirm-password','id':'confirm-password','tabindex':'2','class':'form-control','placeholder':'Confirm Password'}))
	username = forms.CharField(widget=forms.TextInput(attrs=
		{'name':"username",'id':"username",'tabindex':"1",'class':"form-control",'placeholder':"Username"}))
	email = forms.CharField(widget=forms.EmailInput(attrs=
		{'name':"email",'id':"email",'tabindex':"1",'class':"form-control",'placeholder':'Email'}))
	
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
