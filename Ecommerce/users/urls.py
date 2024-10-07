from django.urls import path

from users import views

app_name = "users"


urlpatterns = [
    path('login/', views.login_user, name='login-user'),
    path('register-up/', views.register_user, name='register-user'),
    path('logout-user/', views.logout_user, name='logout-user'),

    path('save-profile-info/', views.save_profile_info, name="save-profile-info"),
    path('save-names/', views.save_names, name="save-names"),

]