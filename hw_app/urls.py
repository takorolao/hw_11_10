from django.urls import path
from .views import items_partial_columns

urlpatterns = [
    path('', items_partial_columns, name='items-partial-columns')
]