from django.shortcuts import render
from downloader.forms import UserInput
from django.http import HttpResponse
from downloader.instadl import get_profile_pic_url
# Create your views here.


def index_view(requests):
    form = UserInput()
    if requests.method == 'POST':
        form = UserInput(requests.POST)
        if form.is_valid():
            try:
                pic_url = get_profile_pic_url(form.cleaned_data['username_ip'])
            except:
                pic_url = ''
            return render(requests, 'main.html', {'url': pic_url})
    return render(requests, 'home.html', {'form': form})
