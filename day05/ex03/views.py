
from django.shortcuts import render
from django.http import HttpResponse
import sys
from .models.movies import Movies

def populate(request) -> HttpResponse:
    data = [
            {
                "episode_nb": 1,
                "title": "The Phantom Menace",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "1999-05-19"
            },
            {
                "episode_nb": 2,
                "title": "Attack of the Clones",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "2002-05-16"
            },
            {
                "episode_nb": 3,
                "title": "Revenge of the Sith",
                "director": "George Lucas",
                "producer": "Rick McCallum",
                "release_date": "2005-05-19"
            },
            {
                "episode_nb": 4,
                "title": "A New Hope",
                "director": "George Lucas",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1977-05-25"
            },
            {
                "episode_nb": 5,
                "title": "The Empire Strikes Back",
                "director": "Irvin Kershner",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1980-05-17"
            },
            {
                "episode_nb": 6,
                "title": "Return of the Jedi",
                "director": "Richard Marquand",
                "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
                "release_date": "1983-05-25"
            },
            {
                "episode_nb": 7,
                "title": "The Force Awakens",
                "director": "J. J. Abrams",
                "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
                "release_date": "2015-12-11"
            }
        ]
    result = []
    for item in data:
        try:
            Movies.objects.create(
                episode_nb = item['episode_nb'],
                title = item['title'],
                director = item['director'],
                producer = item['producer'],
                release_date = item['release_date']
            )
            result.append("OK")
        except Exception as e:
            result.append(e)
            return HttpResponse(e)
    return HttpResponse("<br/>".join(item for item in result))

def display(request) -> HttpResponse:
    try:

        movies = Movies.objects.all()
        if len(movies) > 0:
            return render(request, 'ex03/display.html', {"movies": movies})
        else:
            return HttpResponse("No data available movies")
    except Exception as e:
        with sys.stderr as cerr:
            print(e, file=cerr)
        return HttpResponse(e)