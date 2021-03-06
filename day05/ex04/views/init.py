from django.conf import settings
from django.views import View
from django.http import HttpRequest, HttpResponse
import psycopg2

class Init(View):
    connection = psycopg2.connect(
        database=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )

    def get(self, request):
        try:
            with self.connection.cursor() as query_context:
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
                self.connection.commit()
                # self.connection.close()
            return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(e)