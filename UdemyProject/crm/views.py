from django.shortcuts import render
from .models import Order
from .forms import OrderForm
# Create your views here.
def first_page(request):
    form = OrderForm()
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list' : object_list,
                                            'form' : form})

def thanks_page(reguest):
    name = reguest.POST['name']
    phone = reguest.POST['phone']
    element = Order(order_name= name, order_phone = phone)
    element.save()
    return render(reguest, './thanks_page.html', {'name':name,'phone': phone})
def first_page_1(reguest):
    return render(reguest, './first_page.html')