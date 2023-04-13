from django.shortcuts import render
from .models import Game
# Create your views here.
def gamesHome(request): 
    searchTerm = request.GET.get('searchMovie')
    if searchTerm: 
        games = Game.objects.filter(title__icontains=searchTerm)
    else:
        games = Game.objects.all()
    return render(request, 'gameHome.html', {'searchTerm': searchTerm, 'games': games}) 