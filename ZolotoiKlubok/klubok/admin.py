from django.contrib import admin

from .models import City, Place, Review, Profile

admin.site.register(City)
admin.site.register(Review)
admin.site.register(Profile)
admin.site.register(Place)