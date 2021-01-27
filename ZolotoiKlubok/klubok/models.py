from django.db import models
from django.conf import settings
from django.utils import timezone

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Place(models.Model):
    PLACE_TYPE = [
        ('Park', 'Парк'),
        ('Restaurant', 'Ресторан'),
        ('Cafe', 'Кафе'),
        ('Cinema', 'Кинотеатр'),
        ('Mall', 'Торговый центр'),
        ('Street', 'Улица'),
        ('Square', 'Сквер'),
        ('Sight', 'Достопримечательность'),
    ]
    name = models.CharField('Интересное место', max_length=255)
    desc = models.TextField()
    type = models.CharField('Тип места', max_length=255, choices=PLACE_TYPE, default='Park')
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    place = models.ForeignKey(Place, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.author

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city_from = models.CharField('Откуда', max_length=255)
    age = models.PositiveIntegerField()
    registered_on = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.user
