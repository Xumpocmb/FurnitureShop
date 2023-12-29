from django.urls import path

from .views import profile, user_cart, login, register, logout

app_name = 'users_app'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('user_cart/', user_cart, name='user_cart'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
