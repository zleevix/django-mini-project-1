import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mini_project_1.settings')
django.setup()

import datetime

from home.models import FootballClub, Footballer

FootballClub.objects.create(
    name="Liverpool",
    ground="Anfield",
    capacity=53394,
    manager="Jürgen Klopp",
    nickname="The Reds",
    avarta="images/Liverpool_FC.png",
    league="Premier League",
    founded=datetime.datetime(1892, 6, 3),
    link_detail="https://en.wikipedia.org/wiki/Liverpool_F.C."
)
FootballClub.objects.create(
    name="Chelsea",
    ground="Stamford Bridge",
    capacity=40834,
    manager="Thomas Tuchel",
    nickname="The Blues",
    avarta="images/Chelsea_FC.png",
    league="Premier League",
    founded=datetime.datetime(1905, 3, 10),
    link_detail="https://en.wikipedia.org/wiki/Chelsea_F.C."
)
FootballClub.objects.create(
    name="Arsenal",
    ground="Emirates Stadium",
    capacity=60704,
    manager="Mikel Arteta",
    nickname="The Gunners",
    avarta="images/ArsenalFC.png",
    league="Premier League",
    founded=datetime.datetime(1886, 10, 1),
    link_detail="https://en.wikipedia.org/wiki/Arsenal_F.C."
)
FootballClub.objects.create(
    name="Manchester City",
    ground="Etihad Stadium",
    capacity=55017,
    manager="Pep Guardiola",
    nickname="The Citizens",
    avarta="images/Manchester_City_FC.png",
    league="Premier League",
    founded=datetime.datetime(1880, 1, 1),
    link_detail="https://en.wikipedia.org/wiki/Manchester_City_F.C."
)
FootballClub.objects.create(
    name="Manchester United",
    ground="Old Trafford",
    capacity=74140,
    manager="Ole Gunnar Solskjær",
    nickname="The Red Devils",
    avarta="images/Manchester_United_FC.png",
    league="Premier League",
    founded=datetime.datetime(1902, 1, 1),
    link_detail="https://en.wikipedia.org/wiki/Manchester_United_F.C."
)