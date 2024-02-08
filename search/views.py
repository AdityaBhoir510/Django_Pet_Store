from django.shortcuts import render
from django.views.generic import ListView
from petsapp.models import Pet

# Create your views here.
class SearchQueryView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, ** kwargs):
        context = super(SearchQueryView, self).get_context_data(*args, ** kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects. create(query=query)
        return context

    def get_queryset(self, *args, ** kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        print(query)
        if query is not None:
            return Pet.objects.filter(name_icontains=query)
        return Pet.objects.all()
    
class SearchPetView(ListView):
    template_name = "petsapp/list.html"
    model=Pet

    def get_queryset(self, *args, ** kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('search', None) # method_dict['q']
        print (query)
        if query is not None:
            print('----',query)
            return Pet.pets.search(query)