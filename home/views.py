from django.shortcuts import render
from .models import FootballClub
# Create your views here.

def index(request):
    return render(
        request=request,
        template_name='index.html'
    )

def list_one2many(request):
    clubs = FootballClub.objects.all()
    return render(
        request=request, 
        template_name='list.html',
        context={
            'clubs': clubs
        }
    )