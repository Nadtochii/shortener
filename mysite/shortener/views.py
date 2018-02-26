from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from shortener.models import Shortener
from shortener.forms import ShortForm
import uuid

def short(request):
    error = False
    if request.method == 'POST':
        form = ShortForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            cd = form.cleaned_data
            long_link = cd['long_link']
            short = uuid.uuid4().hex
            link = Shortener.objects.create(long_link=long_link, short_link=short)
            link_id = Shortener.objects.get(id=link.id)
            short_link = 'http://127.0.0.1:8000/' + short
            return render(request, 'shortener/short_form.html', {'long_link': link.long_link, 'short_link': short_link})
        else:
            error = True
    return render(request, 'shortener/short_form.html', {'error': error})


def myredirect(request, short_link):
    link = Shortener.objects.get(short_link=short_link)
    return redirect(link.long_link)
