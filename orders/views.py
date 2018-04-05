from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from .tasks import order_created
from damatex_overseas_app.models import CarousalImages
from cart.cart import Cart
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def order_create(request):
    carosual_images = CarousalImages.objects.all()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # order.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
                # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            #order_created.delay(order.id)  # set the order in the session
            #request.session['order_id'] = order.id  # redirect to the payment
            # return redirect(reverse('orders:order_created', args=order.id))
            return render(request,'orders/order/created.html',{'order': order, 'carosual_images': carosual_images})
    else:
        form = OrderCreateForm()

    return render(request,'orders/order/create.html',{'cart': cart, 'form': form, 'carosual_images': carosual_images})

