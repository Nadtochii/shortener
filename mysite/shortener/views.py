from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from shortener.models import Shortener

# Create your views here.
def make_short(request):
    return render(request, 'shortener/short_form.html')

def short(request):
    error = False
    if 'long_link' in request.GET:
        long_link = request.GET['long_link']
        if not long_link:
            error = True
        else:
            link = Shortener.objects.create(long_link=long_link)
            link_id = Shortener.objects.get(long_link=long_link)
            return render(request, 'shortener/short_form.html', {'long_link': long_link, 'short_link': link_id.id})

    return render(request, 'shortener/short_form.html', {'error': error})

def myredirect(request, link_id):
    link = Shortener.objects.get(id=link_id)
    return redirect(link.long_link)
