from django.urls import path
from .views import * 

urlpatterns = [
    path('', pageView, name='frontpage'),
    path('page/<page>', pageView, name='page')
]

