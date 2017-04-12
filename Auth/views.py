from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from musics.models import Song

# Create your views here.
def home(request):
	songs = Song.objects.order_by('views')[:4]
	return render(request,'Auth/home.html',{'songs':songs})
def logreg(request):
	form1 = LoginForm()
	form2 = RegisterForm() 
	return render(request,'Auth/logreg.html',{'formlog':form1,'formreg':form2})

def Login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				return redirect(home)
			else:
				return HttpResponse('invalid username or password')
		else:
			return HttpResponse("form doesn't valid")

def Register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']

			if password1 == password2:
				user.set_password(password1)
				user.save()
				recent_user = authenticate(username=username,password=password1)
				login(request,recent_user)
				return redirect(home)
			else:
				return HttpResponse("password doesn't match")