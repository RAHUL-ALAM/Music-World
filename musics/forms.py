from django import forms
from .models import Song, Album

class AddAlbumForm(forms.ModelForm):

	name = forms.CharField(max_length=16,widget=forms.TextInput(attrs=
		{'id':"name",'class':"form-control",'placeholder':"Name"}))
	singer = forms.CharField(max_length=16,widget=forms.TextInput(attrs=
		{'id':"singer",'class':"form-control",'placeholder':"singer"}))
	cover = forms.FileField(widget= forms.ClearableFileInput(attrs={'id':"cover"}))

	class Meta:
		model = Album
		fields = ['name','singer','cover']

class AddSongForm(forms.ModelForm):

	title = forms.CharField(max_length=16,widget=forms.TextInput(attrs=
		{'id':"title",'class':"form-control",'placeholder':"Title"}))
	logo = forms.FileField(widget= forms.ClearableFileInput(attrs={'id':"logo"}))
	music = forms.FileField(widget= forms.ClearableFileInput(attrs={'id':"music"}))

	class Meta:
		model = Song
		fields = ['title','logo','music']
