from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Alert
# Si tu as un modèle séparé pour l'historique des prix (PriceHistory ou Price)
# Sinon, change 'sender=Price' par 'sender=Product'
from .models import Product 

@receiver(post_save, sender=Product) 
def check_price_alerts(sender, instance, created, **kwargs):
    """
    Bu fonksiyon, bir ürün güncellendiğinde veya fiyatı değiştiğinde çalışır.
    (Cette fonction se déclenche quand un produit est sauvegardé).
    """
    alerts = Alert.objects.filter(
        product=instance,
        target_price__gte=instance.price,
        # On peut ajouter un statut pour ne pas spammer, ex: is_triggered=False
    )
    
    if alerts.exists():
        print(f"ALARM: {instance.name} için fiyat düştü! {alerts.count()} kullanıcı uyarılacak.")