
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserView)

app_name = 'authentication'
urlpatterns = [

    path('', views.user_form, name='user_insert'),
    path('<int:id>/', views.user_form, name='user_update'),
    path('delete/<int:id>/', views.user_delete, name='user_delete'),
    path('list/', views.user_list, name='user_list'),
    path('app/v1/user/', include(router.urls))

]