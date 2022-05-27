from django.conf import settings
from django.views import View
from django.http import HttpRequest, HttpResponse
import psycopg2

class Init(View):


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
                query_context.execute(
                    """
                    CREATE TABLE IF NOT EXISTS ex04_movies(
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
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(e)
        finally:
            if connection is not None:
                connection.close()