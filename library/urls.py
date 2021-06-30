"""djangoViewTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index

from rest_framework import routers
from rest_framework import permissions
from book import views as book_views
from author import views as author_views
from order import views as order_views
from authentication import views as user_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(
    title="Library API",
    default_version='v1',
    description="Welcome to out library",
),
    public=True,
    permission_classes=(permissions.AllowAny,), )

router = routers.DefaultRouter()

router.register('library/v1/book', book_views.BookView)
router.register('library/v1/author', author_views.AuthorView)
router.register('app/v1/order', order_views.OrderView)
router.register('app/v1/user', user_views.UserView)
router.register('app/v1/user/order', order_views.Order_byUserIDView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('book.urls', namespace='book')),
    path('authors/', include('author.urls', namespace='author')),
    path('users/', include('authentication.urls', namespace='user')),
    path('orders/', include('order.urls', namespace='order')),
    path('', index, name='index'),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0))
]
