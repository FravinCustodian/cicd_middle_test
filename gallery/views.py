from django.shortcuts import render
from .models import Image


def gallery(request):
    images = Image.images()
    return render(request, 'gallery.html', context={'images': images})


def image_detail(request, pk):
    image = Image.get_image(pk)
    return render(request, 'image_detail.html', context={'image': image})
