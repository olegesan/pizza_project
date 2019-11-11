from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("menu/", views.menu, name = "not_a_menu"),
    path('somewhere/', views.menu, name = 'somewhere')
]
