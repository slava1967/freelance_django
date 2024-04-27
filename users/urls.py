from django.urls import path, include

from users import views

urlpatterns = [
    path('', include('main.urls')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('freelancer/', views.freelancer, name='freelancer'),
    path('customer/', views.customer, name='customer'),
    path('<str:user_role>', views.get_user_role, name='user_role'),
    path('profile/', views.profile, name='profile'),
]
