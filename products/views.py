
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Price, Alert

from django.contrib.auth.decorators import login_required
from .forms import AlertForm
from django.dispatch import receiver 
from django.db.models.signals import post_save 



def all_products(request):
    products = Product.objects.all()
    return render(request, 'products/all_products.html', {
        'products': products
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    prices = Price.objects.filter(product_id=pk).order_by('price')
    best_price = prices.first() 

    return render(request, 'products/product_detail.html', {
        'product': product,
        'prices': prices,
        'best_price': best_price,
    })


def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.none()
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        results = Product.objects.none()

    return render(request, 'products/search_product_list.html', {
        'products': products,
        'query': query
    })

@login_required
def dashboard_home(request):
    user_alerts = Alert.objects.filter(user=request.user)
    return render(request, 'dashboard/dashboard_home.html', {'alerts': user_alerts})



@login_required 
def create_alert(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = AlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user # Je lie l'alerte au user connecté
            alert.product = product
            alert.save()
            return redirect('product_detail', pk=product.id)
    else:
        form = AlertForm()
    
    return render(request, 'alerts/alerts_form.html', {'form': form, 'product': product})




@receiver(post_save, sender=Price)
def check_price_alerts(sender, instance, created, **kwargs):
    if created:
        
        Alert.objects.filter(
            product=instance.product,
            target_price__gte=instance.price,
            price_alert=False
        ).update(price_alert=True, last_checked_price=instance.price)


@login_required
def delete_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id, user=request.user)
    alert.delete()
    return redirect('dashboard')


def about(request):
    about_us = Product.objects.all()
    return render(request, 'products/about.html', {
        'products': about_us
    })
def contact(request):
    contact_us = Product.objects.all()
    return render(request, 'products/contact.html', {
        'products': contact_us
    })