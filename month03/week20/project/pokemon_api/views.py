from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon

def pokemon_page(request):
    return render(request, 'pokemon_api/pokemon_list.html')

def pokemon_api(request):
    search = request.GET.get("search", "")
    qs = Pokemon.objects.all()

    if search:
        qs = qs.filter(name__icontains=search)

    data = [{
        "name": p.name,
        "type": p.types.split(",")
    } for p in qs]

    return JsonResponse(data, safe=False)
