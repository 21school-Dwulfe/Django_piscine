# import logging
# from django.http import HttpRequest
# from django.shortcuts import redirect, render
# from django.conf import settings
# from .models import FormHistory 

# def index(request: HttpRequest):
#     logger = logging.getLogger('history')

#     if request.method == 'POST':
#         form = FormHistory(request.POST)
#         if form.is_valid():
#             logger.info(form.cleaned_data['history'])
#         return redirect('/ex02')
#     try:
#         f = open(settings.HISTORY_LOG_FILE, 'r')
#         historys = [line for line in f.readlines()]
#         f.close()
#     except:
#         historys = []

   
#     return render(request, 'ex02/index.html', {'form': FormHistory(), 'historys': historys})

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.conf import settings
from datetime import datetime

from . import forms


def index(request: HttpRequest):

    if request.method == 'POST':
        form = forms.History(request.POST)
        if form.is_valid():
            with open(settings.HISTORY_LOG_FILE, 'a') as out:
                out.write("{1}, {0}\n".format(form.cleaned_data['history'], datetime.now()))
        return redirect('/ex02')
    try:
        f = open(settings.HISTORY_LOG_FILE, 'r')
        historys = [line for line in f.readlines()]
    except Exception as e:
        print(e)
        historys = []

    return render(request, 'ex02/index.html', context={'form': forms.History(), 'historys': historys})