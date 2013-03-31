# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from forpics.imghost.models import Picture
import time
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    latest_picture= Picture.objects.latest('id')
    return render_to_response('index.html', {'latest_picture':latest_picture})

def picture_detail(request, picture_id):
    picture=get_object_or_404(Picture, id=picture_id)
    return render_to_response('image_detail.html', {'picture':picture})

def upload(request):
    if "file" in request.FILES:
        filename = str(int(time.time())) + "." + request.FILES["file"].name.split(".")[-1]
        picture=Picture()
        picture.image.save(filename, request.FILES["file"])
        return HttpResponseRedirect(reverse('imghost.views.picture_detail', args=[picture_id]))
    return HttpResponseRedirect(reverse('imghost.views.index', args=[]))
