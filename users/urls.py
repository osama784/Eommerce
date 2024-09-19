from django.urls import path

from users import views

app_name = "users"


urlpatterns = [
    path('login/', views.login_user, name='login-user'),
    path('register-up/', views.register_user, name='register-user')

]