import sys
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import psycopg2

# Create your views here.
def init(request:HttpRequest):
    try:

        connection = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        with connection.cursor() as query_context:
            query_context.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb int PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
                );
            """)
            connection.commit()
        connection.close()
        return HttpResponse("Ok")
    except Exception as e:
        with sys.stderr as cerr:
            print(e, file=cerr)
        return (HttpRequest(e))