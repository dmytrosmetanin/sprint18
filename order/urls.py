
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('app/v1/order', views.OrderView)
router.register('app/v1/user/order', views.Order_byUserIDView)



app_name = 'order'
urlpatterns = [

    path('', views.order_form, name='order_insert'),
    path('<int:id>/', views.order_form, name='order_update'),
    path('delete/<int:id>/', views.order_delete, name='order_delete'),
    path('list/', views.order_list, name='order_list'),
    path('app/v1/order/', include(router.urls)),
    path('app/v1/user/order/', include(router.urls))

]