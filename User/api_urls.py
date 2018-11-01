from django.urls import path

from User.views import CreateUserView, LoginView

urlpatterns = {
    path('create', CreateUserView.as_view()),
    path('login', LoginView.as_view()),
}