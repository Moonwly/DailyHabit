from django.urls import path

from User.views import CreateUserView, LoginView, Logout

urlpatterns = {
    path('create', CreateUserView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', Logout.as_view()),
}