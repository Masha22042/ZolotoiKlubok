from django.urls import path
from django.contrib.auth import views as auth_views

from .views import index, city_view, add_new_place, place_view, all_places

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('places/all/', all_places, name='all_places'),
    path('<str:city>/', city_view, name='city_view'),
    path('<str:city>/new/', add_new_place, name='new_place'),
    path('<str:city>/<str:place>/', place_view, name='place_view'),
]
