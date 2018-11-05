from django.urls import path, include

urlpatterns = {
    path('user/', include('User.api_urls')),
    path('goal/', include('Goal.api_urls')),
    path('record/', include('Record.api_urls')),
    path('weight/', include('Weight.api_urls')),
    # path('Account', include('Account.api_urls')),
}