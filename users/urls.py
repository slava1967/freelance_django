from django.urls import path, include

from users import views

urlpatterns = [
    path('', include('main.urls')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('freelancer_dashboard/', views.freelancer, name='freelancer'),
    path('customer_dashboard/', views.customer, name='customer'),
    path('profile/', views.profile, name='profile'),
]
