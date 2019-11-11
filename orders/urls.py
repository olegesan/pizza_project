from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("menu/", views.menu, name = "menu"),
    path('/somewhere/', views.menu, name = 'somewhere'),
    path('signup/', views.signup_page, name = 'signup' ),
    path('signup/new/', views.signup_new, name = 'signup_new'),
    path('login/', views.login_page, name = 'login'),
    path('login/func/', views.login_func, name = 'login_func'),
    path('logout/', views.logout_page, name = 'logout'),
    path('logout/func/', views.logout_func, name = 'logout_func')
    # path('profile/<int:user_id>', view.profile_open, name='profile')
]
