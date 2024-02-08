from django.urls import path
from petsapp import views

app_name = "petsapp"
urlpatterns = [
    path("pets/", views.PetListView.as_view(),name='pets'),
    path("petlist/", views.pet_list_view.as_view()),
    path("rangelist/", views.pet_range_list_view),
    path("expensivepet/", views.expensive_pet_list_view),
    path("doglist/", views.DogsListView.as_view()),
    path("catlist/", views.CatsListView.as_view()),
    path("<pk>/", views.PetDetailView.as_view()),
    path("pets/<slug:slug>/", views.PetDetailSlugView.as_view()),
    
    # path("searchview/", views.SearchPetView.as_view()),
]
