from django import forms
from .models import Song, Album

class AddAlbumForm(forms.ModelForm):

	class Meta:
		model = Album
		fields = ['name','singer','cover']

class AddSongForm(forms.ModelForm):

	class Meta:
		model = Song
		fields = ['title','logo','music']
