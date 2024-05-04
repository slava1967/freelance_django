from django.contrib.auth import views as auth_views
from django.urls import path, include

from users import views

urlpatterns = [
    path("", include("main.urls")),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path("freelancer/", views.freelancer, name="freelancer"),
    path("customer/", views.customer, name="customer"),
    # path("<str:user_role>", views.get_user_role, name="user_role"),
    path("profile/", views.profile, name="profile"),
]
