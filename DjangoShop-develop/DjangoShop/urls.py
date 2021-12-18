"""DjangoShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from mainApp import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', authViews.LogoutView.as_view(next_page='product_list'), name='logout'),
    path('product_list', views.index, name="product_list"),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('show_cart', views.show_cart, name='show_cart'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
    path('order',views.order, name='order' ),
]
