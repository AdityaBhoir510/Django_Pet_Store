from django.urls import path
from petsapp import views
from .views import SearchPetView, SearchQueryView
from petsapp.views import DogsListView, CatsListView

app_name = "search"
urlpatterns = [
    path('dog_list/', DogsListView.as_view(), name='Doglist'),
    path('cat_list/', CatsListView.as_view(), name='Catlist'),
    path('searchqview/', SearchQueryView.as_view(), name="q"),
    path('searchview/', SearchPetView.as_view(), name="query"),
]