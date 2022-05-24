from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest, HttpResponse
import sys
import psycopg2


def init(request)->HttpResponse:
    try:
        connection = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        with connection.cursor() as query_context:
            query_context.execute(
                """
                CREATE TABLE IF NOT EXISTS ex02_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
                );
                """
            )
        connection.commit()
        connection.close()
        return HttpResponse("OK")
    except Exception as e:
        with sys.stderr as cerr:
            print(e, file=cerr)
        return HttpResponse(e)

def populate(request):
    try:
        connection = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        
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
        with connection.cursor() as query_context:
            with open('populate.log', 'a') as output:
                for item in data:
                    sql =  """INSERT INTO ex02_movies (
                        episode_nb, 
                        title, 
                        director, 
                        producer, 
                        release_date
                        ) VALUES ('{}', '{}', '{}', '{}', '{}');""".format(
                            item['episode_nb'], 
                            item['title'], 
                            item['director'],
                            item['producer'],
                            item['release_date'])               
                    query_context.execute(sql)
                    output.write(sql+"\n")
                    result.append("OK")
                    connection.commit()
        return HttpResponse("<br/>".join(item for item in result))  
    except Exception as e:
        print(e)
        return HttpResponse(e)

def display(request):
    try:
        connection = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        with connection.cursor() as query_context:
            query_context.execute("SELECT * FROM ex02_movies")
            movies = query_context.fetchall()
            if movies:
                return render(request, 'ex02/display.html', {"movies":movies})
            else:
                return HttpResponse("No data available")
    except Exception as e:
        with sys.stderr as cerr:
            print(e, file=cerr)
        return HttpResponse(e)
