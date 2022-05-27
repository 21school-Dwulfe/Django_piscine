from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from ..forms import UpdateForm
import sys
import psycopg2

class Update(View):
    template = "ex06/update.html"
  
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
                query_context.execute("SELECT * FROM ex06_movies;")
                movies = query_context.fetchall()
                connection.close()
            if movies:
                return render(request, self.template, {"form" : UpdateForm(choices=(
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
                query_context.execute("SELECT * FROM ex06_movies;")
                movies = query_context.fetchall()
                choices = ((movie[0], movie[0]) for movie in movies)    
                data = UpdateForm(choices, request.POST)
                SQL = f"""UPDATE ex06_movies SET opening_crawl = %s WHERE title = %s
                """
                if data.is_valid() == True:
                    with self.connection.cursor() as query_context:
                        query_context.execute(SQL, [
                            data.cleaned_data['opening_crawl'], 
                            data.cleaned_data['title']])
                    connection.commit()
            return redirect(request.path)
        except Exception as e:
            print(e)
        finally:
                if connection is not None:
                    connection.close()