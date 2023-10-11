from django.shortcuts import render
from .models import Item

def items_partial_columns(request):
    items = Item.objects.values('price', 'name')
    return render(request, 'items_partial_columns.html', {'items': items})
