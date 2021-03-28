from django.db import models

# Create your models here.

class FootballClub(models.Model):
    name = models.CharField(max_length=30)
    ground = models.CharField(max_length=100)
    capacity = models.IntegerField()
    manager = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    avarta = models.ImageField()
    founded = models.DateField()
    league = models.CharField(max_length=100)
    link_detail = models.CharField(max_length=100)
    class Meta:
        db_table = "FootballClub"

class Footballer(models.Model):
    GOALKEEPER = "GOALKEEPER"
    DEFENDER = "DEFENDER"
    MIDFIELDER = "MIDFIELDER"
    ATTACKER = "ATTACKER"
    DEFAULT = "FOOTBALLER"
    POSITION_IN_CLUB = [
        (GOALKEEPER, "GOALKEEPER"),
        (DEFENDER, "DEFENDER"),
        (MIDFIELDER , "MIDFIELDER"),
        (ATTACKER, "ATTACKER"),
    ]

    fullname = models.CharField(max_length=100)
    birthday = models.DateTimeField()
    height = models.IntegerField()
    position = models.CharField(
        max_length=10,
        choices=POSITION_IN_CLUB,
        default=DEFAULT
    )
    current_club = models.ForeignKey(FootballClub, on_delete=models.CASCADE)

    class Meta:
        db_table = "Footballer"