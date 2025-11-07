from django.shortcuts import render

# Create your views here.
def pokemon_list(request):
    return render(request, 'pokemon_api/pokemon_list.html')