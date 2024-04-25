from django.urls import path, include

from users import views

urlpatterns = [
    path('', include('main.urls')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/freelancer/', views.freelancer, name='freelancer'),
    path('dashboard/customer/', views.customer, name='customer'),
    path('dashboard/<str:user_role>', views.get_user_role, name='user_role'),
    path('profile/', views.profile, name='profile'),
]
