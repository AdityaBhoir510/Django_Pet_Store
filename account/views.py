from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from cart.models import Cart
from petsapp.models import Pet
 
# Create your views here.

def about_page(request):
    return render(request,"base/about_page.html")

def service_page(request):
    return render(request,"base/service_page.html")

def register_page(request):
    form=RegisterForm()
    context = {
        "title":"Registration Page",
        "form":form
    }
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            user.set_password(user.password)
            user.save()
            return redirect('/login')
        else:
            return render(request, "base/register.html", context)
    return render(request, "base/register.html", context)

def login_page(request):
    loginform=AuthenticationForm()
    if request.method == 'POST':
        username=request.POST.get('username' )
        pwd=request.POST.get('password' )
        print(username, pwd)
        user=authenticate(username=username, password=pwd)
        print(user)
        if user != None:
            login(request, user)
            print(request, user)
            return redirect('/')
        else:
            msg='Invalid username or password'
            return render(request, 'base/login.html', {'form': loginform, 'msg':msg})

    return render(request, 'base/login.html', {'form':loginform})

def logOut(request):
    print(request.user)
    logout(request)
    print(request.user)
    return redirect('/')

class PetListView(ListView):
    queryset = Pet.objects.all()
    template_name = "petsapp/list.html"

#function based view
def pet_list_view(request):
    queryset = Pet.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "petsapp/list.html", context)



#class based view
class PetDetailView(DetailView):
    queryset = Pet.objects.all()
    print("default Manager",queryset)
    pet_data = Pet.pets.all()   
    print("custom Manager",pet_data)
    template_name = "petsapp/detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(PetDetailView, self).get_context_data(*args, **kwargs)
       # print(context)
        return context

def pet_detail_view(request, pk=None, *args, **kwargs):

    #instance = Pet.objects.get(pk=pk) #id
    # instance = get_object_or_404(Pet, pk=pk)
    #context = {
    #    'object': instance
    #}
    
    qs  = Pet.objects.filter(id=pk)	
    #print(qs)
    #print(Pet_data)
    if qs.exists() and qs.count() == 1: # len(qs)
        instance = qs.first()
    else:
        raise Http404("Pet doesn't exist")

    context = {
        'object': instance
    }
    return render(request, "petsapp/detail.html", context)



def pet_range_list_view(request):
    queryset = Pet.pets.get_pets_price_range(10000, 20000)
    context = {
        'object_list': queryset
    }
    return render(request, "petsapp/list.html", context)


class DogsListView(ListView):
    template_name = "petsapp/list.html"

    def get_queryset(self, *args, **kwargs):
        #request = self.request
        return Pet.pet.dog_list()

class CatsListView(ListView):
    template_name = "petsapp/list.html"

    def get_queryset(self, *args, **kwargs):
        #request = self.request
        return Pet.pet.cat_list()


class PetDetailSlugView(DetailView):
    print("=====")
    model=Pet
    queryset = Pet.objects.all()
    template_name = "Petsapp/detail.html"
    slug_field='slug'
   
    def get_object(self, *args, **kwargs):
        request = self.request
        print(request)
        slug = self.kwargs.get('slug')
        print("slug",slug)
        instance = get_object_or_404(Pet, slug=slug, active=True)
        try:
            instance = Pet.objects.get(slug=slug)
            
            cartid=request.session.session_key
            incart= Cart.objects.filter(cart_id=cartid,pet=instance).exists()
            context={'incart':incart,'petobject':instance}
            print(incart,cartid)
            print(instance)
        except Pet.DoesNotExist:
            raise Http404("Not found..")
        except Pet.MultipleObjectsReturned:
            qs = Pet.objects.filter(slug=slug)
            instance = qs.first()
        except Exception as e:
           
            raise Http404("Errror ",e)
        
        return instance