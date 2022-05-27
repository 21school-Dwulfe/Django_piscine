from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from ..models import Movies


class Display(View):
    template = 'ex07/display.html'

    def get(self, request):
        try:
            movies = Movies.objects.all()
            if len(movies) > 0:
                return render(request, self.template, {"movies": movies})
            else:
                return HttpResponse("No data available movies")
        except Exception as e:
            return HttpResponse(e)