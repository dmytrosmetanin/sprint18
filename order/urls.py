
from django.urls import path, include
from . import views

app_name = 'order'
urlpatterns = [

    path('', views.order_form, name='order_insert'),
    path('<int:id>/', views.order_form, name='order_update'),
    path('delete/<int:id>/', views.order_delete, name='order_delete'),
    path('list/', views.order_list, name='order_list'),

]