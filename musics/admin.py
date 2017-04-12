from django.contrib import admin
from .models import Song, Album, Like, View
# Register your models here.
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Like)
admin.site.register(View)