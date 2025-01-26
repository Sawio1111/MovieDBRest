from peewee import *

from database import db

class BaseModel(Model):
    class Meta:
        database = db

class Actor(BaseModel):
    name = CharField()
    surname = CharField()

class Movie(BaseModel):
    title = CharField()
    director = CharField(null=True)
    year = IntegerField()
    description = TextField(null=True)
    actors = ManyToManyField(Actor, backref='movies')

ActorMovie = Movie.actors.get_through_model()

db.connect()
db.create_tables([Actor, Movie, ActorMovie], safe=True)


actor1 = Actor.create(name="Leonardo", surname="DiCaprio")
actor2 = Actor.create(name="Morgan", surname="Freeman")
actor3 = Actor.create(name="Robert", surname="De Niro")
actor4 = Actor.create(name="Scarlett", surname="Johansson")
actor5 = Actor.create(name="Tom", surname="Hanks")


movie1 = Movie.create(title="Inception", director="Christopher Nolan", year=2010, description="A mind-bending thriller.")
movie2 = Movie.create(title="The Shawshank Redemption", director="Frank Darabont", year=1994, description="Hope is a good thing.")
movie3 = Movie.create(title="The Irishman", director="Martin Scorsese", year=2019, description="An epic gangster saga.")
movie4 = Movie.create(title="Lost in Translation", director="Sofia Coppola", year=2003, description="A story of loneliness and connection.")
movie5 = Movie.create(title="Forrest Gump", director="Robert Zemeckis", year=1994, description="Life is like a box of chocolates.")


movie1.actors.add([actor1, actor4])  
movie2.actors.add([actor2])          
movie3.actors.add([actor3, actor1])
movie4.actors.add([actor4])         
movie5.actors.add([actor5, actor2]) 

db.close()