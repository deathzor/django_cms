from django.urls import path
from .views import *

urlpatterns = [
        path('fit/<int:fitid>', fitView, name='fit'),
        path('<int:doctrineId>', doctrineView, name="doctrine fit overview"),
        path('', doctrineView, name='doctrine overview')

]

