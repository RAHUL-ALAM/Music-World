from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$',views.musics_home),
	url(r'^(?P<album_id>[0-9]+)/$',views.detailAlbum),
	url(r'^(?P<album_id>[0-9]+)/(?P<song_id>[0-9]+)$',views.detailSong),
]