from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User


from .models import City, Place, Review
from .forms import PlaceForm, ReviewForm
# Create your views here.

def index(request):
    cities = City.objects.all()
    return render(request, 'klubok/index.html', {'cities': cities})

def city_view(request, city):
    city_name = get_object_or_404(City, name=city)
    places = city_name.place_set.all()
    return render(request, 'klubok/cityview.html', {'city_name': city_name, 'places': places})

def add_new_place(request, city):
    city_name = get_object_or_404(City, name=city)
    new_place = None
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            new_place = form.save(commit=False)
            new_place.city = city_name
            new_place.save()
            return redirect(city_name.get_absolute_url())
    else:
        form = PlaceForm()

    return render(request, 'klubok/new_place.html', {'city_name': city_name, 'form': form})

def place_view(request, city, place):
    city_name = get_object_or_404(City, name=city)
    place_name = get_object_or_404(Place, name=place)
    reviews = Review.objects.filter(place_id=place_name.id)
    new_review = None
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.author = User.objects.get(username=request.user.username)
            new_review.place = place_name
            new_review.save()
    else:
        form = ReviewForm()
    return render(request, 'klubok/place_view.html', {'city_name': city_name, 'place_name': place_name, 'reviews': reviews,
                                                      'form': form})


def all_places(request):
    places = Place.objects.all()
    return render(request, 'klubok/places.html', {'places': places})