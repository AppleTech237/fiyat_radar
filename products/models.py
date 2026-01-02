from django.db import models
from stores.models import Store
from django.contrib.auth.models import User

#PRODUCTS
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


#PRICES
class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    store = models.ForeignKey(Store, on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url_on_store = models.URLField(max_length=500, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.price} ({self.store.name})" 


#CATEGORIES
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#ALERTS
class Alert(models.Model):
    # We link an alert to a user and produit
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_alerts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='alerts')
    
    # price is < than targetprice; customer receive  ALERT
    target_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # To know if the ALERT PRICE is still ACTIVE
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    price_alert = models.BooleanField(default=False) # Devient True quand le prix baisse
    last_checked_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Alert for {self.user.username} on {self.product.name}"
    
  
    
