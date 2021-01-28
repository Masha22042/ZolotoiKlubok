from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("city_view", kwargs={"city": self.name})
    

class Place(models.Model):
    PLACE_TYPE = [
        ('Парк', 'Парк'),
        ('Ресторан', 'Ресторан'),
        ('Кафе', 'Кафе'),
        ('Кинотеатр', 'Кинотеатр'),
        ('ТРЦ', 'Торговый центр'),
        ('Улица', 'Улица'),
        ('Сквер', 'Сквер'),
        ('Достопримечательность', 'Достопримечательность'),
    ]
    name = models.CharField('Название', max_length=255)
    desc = models.TextField('Описание')
    type = models.CharField('', max_length=255, choices=PLACE_TYPE, default='Парк')
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("place_view", kwargs={"city": self.city.name, 'place': self.name})
    

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    place = models.ForeignKey(Place, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.author.username

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city_from = models.CharField('Откуда', max_length=255)
    age = models.PositiveIntegerField()
    registered_on = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.user.username
