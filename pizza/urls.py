"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("orders.urls")),
    path("menu/", include("orders.urls")),
    path('signup/', include('orders.urls')),
    path('login/', include('orders.urls')),
    path('<str:user>',include('orders.urls')),
    path('<str:user>/edit/', include('orders.urls')),
    path('<str:user>/cart/', include('orders.urls')),
    path('api/get/', include('orders.urls')),
    path('<str:user>/order/', include('orders.urls')),

]
