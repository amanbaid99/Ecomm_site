from .models import *

def cartData(request):
    user=request.user
    order,created=Order.objects.get_or_create(user=user,complete=False)
    items = order.orderitem_set.all()
    cartItems=order.get_cart_items

    return{'cartItems':cartItems,'order':order,'items':items}