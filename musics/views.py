from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Song, Album, Like, View
from .forms  import AddAlbumForm, AddSongForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def musics_home(request):
	if request.method=="POST":
		user = request.user
		form = AddAlbumForm(request.POST,request.FILES)
		if form.is_valid():
			alBum = form.save(commit=False)
			alBum.user = user
			alBum.save()
		else:
			return HttpResponse("form not valid")
	form = AddAlbumForm()
	all_album = Album.objects.all()
	return render(request,'musics/musics_home.html',{'all_album':all_album,'form':form})




def detailAlbum(request,album_id):
	if request.method == "POST":
		form = AddSongForm(request.POST,request.FILES)
		if form.is_valid():
			album = Album.objects.get(id=album_id)
			song = form.save(commit=False)
			song.album = album
			song.save()
		else:
			return HttpResponse("not valid form")

	form = AddSongForm()
	user = request.user
	try:
		album = Album.objects.get(id=album_id)
		songs = Song.objects.filter(album_id=album_id)
	except Album.DoesNotExist:
		return HttpResponse("album doesnot exist")
	return render(request,'musics/detailAlbum.html',
		{'user':user,'form':form,'songs':songs,'album_id':album_id,'album':album})




def detailSong(request,album_id,song_id):
	album = Album.objects.get(id=album_id)
	song = Song.objects.get(id=song_id)
	song.views = song.views + 1
	song.save()
	if request.user.is_authenticated():
		try:
			viewsbyuser = View.objects.get(user=request.user,song=song)
			viewsbyuser.views = viewsbyuser.views + 1
			viewsbyuser.save()
		except View.DoesNotExist:
			viewobj = View()
			viewobj.user = request.user
			viewobj.song = song
			viewobj.views = 1
			viewobj.save()
	if request.user.is_authenticated():
		isLiked = Like.objects.filter(song=song,user=request.user)
		if request.method == "POST":
			if isLiked:
				isLiked.delete()
			else:
				likeobj = Like()
				likeobj.user = request.user
				likeobj.song = song
				likeobj.is_liked = 1
				likeobj.save()

	likes = Like.objects.filter(song=song).count()
	views = song.views
	context = {'album':album,'song':song,'likes':likes,'views':views}
	if request.user.is_authenticated():
		isLiked = Like.objects.filter(song=song,user=request.user)
		if isLiked:
			isliked = 1
		else:
			isliked = 0
		context.update({'is_liked':isliked})
	if request.user.is_authenticated():
		viewsbyu = View.objects.get(user=request.user,song=song).views
		context.update({'viewsbyuser':viewsbyu})

	return render(request,"musics/detailSong.html",context)

