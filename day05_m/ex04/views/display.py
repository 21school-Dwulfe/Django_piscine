
import sys
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import psycopg2

class Display(View):
    template = 'ex04/display.html'
   
    def get(self, request) ->HttpResponse:
        try:
            connection = psycopg2.connect(
                database=settings.DATABASES['default']['NAME'],
                user=settings.DATABASES['default']['USER'],
                password=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST'],
                port=settings.DATABASES['default']['PORT']
            )
            with connection.cursor() as query_context:
                query_context.execute("SELECT * FROM ex04_movies;")
                movies = query_context.fetchall()
            if movies:
                return render(request, self.template, {"movies" : movies})
            return HttpResponse("No data available")
        except Exception as e:
            with sys.stderr as cerr:
                print(e, file=cerr)
            return HttpResponse(e)
        finally:
            if connection is not None:
                connection.close()


