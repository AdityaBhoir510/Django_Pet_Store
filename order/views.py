from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from .models import OrderPet, Orders, Payment
from django.core.mail import EmailMessage
from .forms import OrdersForm
from cart.models import Cart
from datetime import date
import json

# Create your views here.
def place_order(request):
    form=OrdersForm()
    current_user=request.user
    cart_item=Cart.objects.filter(user=current_user)
    cart_item_count=cart_item.count()
    total_amount=request.GET.get('totalamount') # fetch total amount from request object
    print("place order",total_amount)
    if cart_item_count <= 0:
        return redirect('pets:petlist')
    if request.method == 'POST':
        form=OrdersForm(request.POST)
        data=Orders()
        print(total_amount,request.POST)
        if form.is_valid():
            data.user=request.user
            data.first_name=form.cleaned_data.get('first_name')
            data.last_name=form.cleaned_data.get('last_name')
            data.phone=form.cleaned_data.get('phone')
            data.email=form.cleaned_data.get('email')
            data.address=form.cleaned_data.get('address')
            data.country=form.cleaned_data.get('country')
            data.state=form.cleaned_data.get('state')
            data.city=form.cleaned_data.get('city')
            data.total=total_amount
            data.ip=request.META.get('REMOTE_ADDR')
            todaydate = date.today()
            data.save()
            
            today=str(todaydate). replace('-','')
            ordernumber=today+str(data.id)#genrating order number
            data.order_number=ordernumber
            data.save()
            
            order_object = Orders.objects.get(user=request.user,order_number=ordernumber)
            print(ordernumber,order_object)
            context={'orders':order_object,'cart_item':cart_item,'total':total_amount}
            
            return render(request,'orders/payment_page.html',context)
    return render(request,'orders/billing_page.html',{'form':form, 'total':total_amount})

@csrf_exempt
def payments(request):
    body=json.loads(request.body)
    order=Orders.objects.get(user=request.user, order_number=body['orderId'])
    payment=Payment(
        payment_id=body['transactionId'],
        user=request.user,
        amount_paid=order.total,
        status=body['status']
    )
    payment.save()
    # Orders.payment=payment
    # Orders.save()
    Orders.objects.update(payment=payment)
    #move cart items n OrderPet
    cart_items=Cart.objects.filter(user=request.user)
    for item in cart_items:
        orderpet=OrderPet()
        orderpet.order=order
        orderpet.payment=payment
        orderpet.user_id=request.user.id
        orderpet.pet=item.pet
        orderpet.quantity=item.quantity
        orderpet.pet_price=item.pet.price
        orderpet.is_orderd=True
        orderpet.save()
        #delete item from cart
        item.delete()
    #Email Order details
    mail_subject= 'Thank you for yur order'
    message= render_to_string('orders/order_email.html', context={'user':request.user, 'order':order, 'title':'Order.Placed'})
    to_email=request.user.email
    send_email=EmailMessage(mail_subject,message, to=[to_email])
    send_email.send()
    # return render(request, 'orders/payment_page.html')
    return JsonResponse({'trasid':payment.payment_id,'order_num':order.order_number})

def order_completed(request):
    order_number=request.GET.get('order_number')
    transid=request.GET.get('paymentid')
    return render(request, 'orders/order_complete.html', {'transid':transid, 'order_number':order_number})