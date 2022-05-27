from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from ..forms import RemoveForm
import sys
import psycopg2

class Remove(View):
    template = "ex04/remove.html"
   
    def get(self, request):
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
                return render(request, self.template, {"form" : RemoveForm(choices=(
                    (movie[0], movie[0]) for movie in movies))})
            else:
                return HttpResponse("No data available")
        except Exception as e:
            with sys.stderr as cerr:
                print(e, file=cerr)
            return HttpResponse(e)
        finally:
            if connection is not None:
                connection.close()

    def post(self, request):
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
                choices = ((movie[0], movie[0]) for movie in movies)    
                data = RemoveForm(choices, request.POST)
                SQL = f"""DELETE FROM ex04_movies WHERE title = %s
                """
                if data.is_valid() == True:
                    with connection.cursor() as query_context:
                        query_context.execute(SQL, [data.cleaned_data['title']])
                    connection.commit()
        except Exception as e:
            print(e)
        finally:
            if connection is not None:
                connection.close()
        return redirect(request.path)