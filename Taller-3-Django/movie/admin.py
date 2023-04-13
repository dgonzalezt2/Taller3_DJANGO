from django.contrib import admin
from .models import Movie, Review
from games.models import Game
# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Game)

