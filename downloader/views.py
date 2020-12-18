from django.shortcuts import render
from downloader.forms import UserInput
from downloader.instadl import get_insta_user_data
# Create your views here.


def index_view(requests):
    form = UserInput()
    if requests.method == 'POST':
        form = UserInput(requests.POST)
        if form.is_valid():
            try:
                user_data = get_insta_user_data(
                    form.cleaned_data['username_ip'])
            except:
                user_data = ''
            return render(requests, 'main.html', {'user_data': user_data})
    return render(requests, 'home.html', {'form': form})
