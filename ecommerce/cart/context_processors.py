from cart.models import cart

def productcount(request):
    item_count=0
    if request.user.is_authenticated:
        u=request.user
        try:
            car=cart.objects.filter(user=u)
            for i in car:
                item_count=item_count+i.quantity
        except:
            item_count=0
    return {'count':item_count}
