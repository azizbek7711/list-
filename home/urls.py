
from django.urls import path
from .views import *
urlpatterns = [
    path('',student,name= 'student' ),
    path('talaba/', talaba, name = 'talaba'),
    path('talaba-delete/<int:pk>/', talaba_delete, name = 'talaba-delete'),
    path('talaba-update/<int:pk>/', talaba_update, name = 'talaba-update'),
    path('order/', order, name = 'order'),
    path('order-delete/<int:pk>/', order_delete, name = 'order-delete')
]
