from django.urls import path

from Weight.views import NewWeightView, GetWeightView

urlpatterns = {
    path('new_weight', NewWeightView.as_view()),
    path('get_weight', GetWeightView.as_view()),
}