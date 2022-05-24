from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from ..forms import RemoveForm, UpdateForm
from ..models import Movies
import sys
import psycopg2

class Update(View):
    template = "ex07/update.html"
 
    def get(self, request):
        try:
            movies = Movies.objects.all()
            if movies:
                return render(request, self.template, {"form" : UpdateForm(choices=(
                    (movie.title, movie.title) for movie in movies))})
            else:
                return HttpResponse("No data available")
        except Exception as e:
            with sys.stderr as cerr:
                print(e, file=cerr)
            return HttpResponse(e)

    def post(self, request):
        try:
            movies = Movies.objects.all()
            choices = ((movie.title, movie.title) for movie in movies)    
            data = UpdateForm(choices, request.POST)
            if data.is_valid() == True:
               instance = Movies.objects.get(title=data.cleaned_data['title'])
               instance.opening_crawl = data.cleaned_data['opening_crawl']
               instance.save()
        except Exception as e:
            print(e)
        return redirect(request.path)