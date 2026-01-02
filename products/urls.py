from django.urls import path
from . import views


urlpatterns = [
    
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('search/', views.search_products, name='search_products'),
    path('dashboard/', views.dashboard_home, name='dashboard'),
    path('add/<int:product_id>/', views.create_alert, name='create_alert'),
    path('delete-alert/<int:alert_id>/', views.delete_alert, name='delete_alert'),
    path('all_products/', views.all_products, name='all_products'),

]
