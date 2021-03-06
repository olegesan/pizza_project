from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("menu/", views.menu, name = "menu"),
    path('signup/', views.signup, name = 'signup' ),
    path('login/', views.login_page, name = 'login'),
    path('login/func/', views.login_func, name = 'login_func'),
    path('logout/', views.logout_page, name = 'logout'),
    path('logout/func/', views.logout_func, name = 'logout_func'),
    path('orders/', views.order, name = 'orders'),
    path('<str:user>/', views.profile_open, name = 'profile'),
    path('<str:user>/edit/', views.profile_edit, name = 'profile_edit'),
    path('<str:user>/cart/', views.cart, name = 'cart'),
    path('cart/api/', views.cart_api, name = 'cart_api'),
    path('<str:user>/order/', views.order_api, name = 'order_api'),
    path('orders/api/', views.order_api, name = 'order_api'),


    # path('profile/<int:user_id>', view.profile_open, name='profile')
]
