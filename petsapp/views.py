from django.shortcuts import render,HttpResponse
from django.http import Http404
from django.views.generic import ListView,DetailView
from .models import Pet

# Create your views here.
class PetListView(ListView):
    queryset = Pet.objects.all()
    template_name = "petsapp/list.html"

class pet_list_view(ListView):
    pass

def pet_range_list_view(request):
    queryset = Pet.pets.get_pets_price_range(10000, 20000)
    context = {
    'object_list': queryset
    }
    return render(request, "petsapp/list.html", context)

def expensive_pet_list_view(request):
    queryset = Pet.pets.expensive_pets_view()
    context = {
    'object_list': queryset
    }
    return render(request, "petsapp/list.html", context)

class DogsListView(ListView):
    template_name = "petsapp/list.html"

    def get_queryset(self, *args, ** kwargs):
        #request = self.request
        return Pet.pet.dog_list()

class CatsListView(ListView):
    template_name = "petsapp/list.html"

    def get_queryset(self, *args, ** kwargs):
        #request = self.request
        return Pet.pet.cat_list()

class PetDetailSlugView(DetailView):
    model = Pet
    template_name = 'petsapp/detail.html'
    context_object_name = 'pet'
    
    def get_object(self, *args,**kwargs):
        request = self.request
        print(request)
        slug = self.kwargs.get('slug')
        print("slug",slug)
        #instance = get_object_or_404(Pet, slug=slug, active=True)
        try:
            instance = Pet.objects.get(slug=slug)
            print(instance)
        except Pet. DoesNotExist:
            raise Http404("Not found .. ")
        except Pet.MultipleObjectsReturned:
            qs = Pet.objects.filter(slug=slug)
            instance = qs.first()
        except Exception as e:
            raise Http404("Errror ",e)
        return instance
            
class PetDetailView(DetailView):
    queryset = Pet.objects.all()
    template_name = "petsapp/detail.html"

    def get_context_data(self, *args, ** kwargs):
        context = super(PetDetailView, self).get_context_data(*args, ** kwargs)
        # print(context)
        return context