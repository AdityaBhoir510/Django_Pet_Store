from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Cart
from django.db.models import Sum
from petsapp.models import Pet

# Create your views here.
def cart_home(request):
    items = Cart.objects.filter(user = request.user)
    flag = items.exists
    amt = items.aggregate(Sum('totalprice'))
    totalamt=amt['totalprice__sum']
    print(totalamt)
    # request.session['cart_id']=12
    # request.session['user']=request.user.username
    
    return render(request,"cart/home.html",{'items':items,'flag':flag,'totalamt':totalamt})

def update_cart(request):
    p=request.POST.get('price')
    q=request.POST.get('qnt')
    print(request.POST)
    id=request.POST.get('cid')
    totalprice=float(p)*int(q)
    Cart.objects.filter(id=id).update(quantity=q, totalprice=totalprice)
    total=Cart.objects.filter(user=request.user).aggregate(Sum('totalprice'))
    print(total)

    totalamount=total['totalprice__sum']
    Cart.amount=totalamount

    return JsonResponse({'status': True, 'totalprice': totalprice, 'totalam': Cart.amount})

def add_to_cart(request,id):
    cart_id=request.session.session_key
    if cart_id == None:
        cart_id=request.session.create()
        print(cart_id)
        
    pet=Pet.objects.get(id=id)
    price=pet.price
    user=request.user

    Cart(cart_id=cart_id,pet=pet,user=user, totalprice=price).save()

    return redirect('petsapp:pets')

def delete_cart(request,id) :
    cart=Cart.objects.get(id=id)
    cart.delete()
    return redirect('cart:cartpage' )