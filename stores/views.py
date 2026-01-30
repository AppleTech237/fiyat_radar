from django.shortcuts import render
from stores.models import Store 

def store_list(request):
    all_stores = Store.objects.all()
    return render(request, 'stores/store_list.html', {'stores': all_stores})