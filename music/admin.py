from django.contrib import admin

from .models import Album, Song

class SongInline(admin.TabularInline):		#Row level view
	model = Song
	extra = 3

class AlbumAdmin(admin.ModelAdmin): 			#Table level view
	list_display = ('artist','album_title','genre','album_logo','pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['artist','album_title','genre','album_logo']
	inlines = [SongInline]

class SongAdmin(admin.ModelAdmin):			#table level view
	list_display = ('file_type','song_title','file', 'album')
	actions = ['custom_delete_selected']

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
