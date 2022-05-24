
from django.conf import settings
from django.http.response import HttpResponse
from django.views import View
import psycopg2

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

class Populate(View):
    connection = psycopg2.connect(
        database=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )

    def get(self, request):
        result = []
        with self.connection.cursor() as query_context:
            for item in data:
                sql =  """INSERT INTO ex06_movies (
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
                result.append("OK")
                self.connection.commit()
            self.connection.close()
        return HttpResponse("<br/>".join(item for item in result)) 