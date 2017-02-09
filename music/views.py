from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from muzy.settings import MUSIC_URL

from .models import Album, Song

def index(request):
    latest_album_list = Album.objects.order_by('-pub_date')[:5]
    context = {'latest_album_list': latest_album_list}
    return render(request, 'index_music.html', context)

def detail(request, album_id):
    try:
        all_albums = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("album does not exist")
        return render(request, 'detail_music.html', {'error_message': "Not a proper album"})
    songs = Song.objects.filter(album=all_albums)   
    return render(request, 'detail_music.html', {'MUSIC_URL':MUSIC_URL, 'album': all_albums, 'songs': songs})

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()		
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
#            for f in files:
#                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)