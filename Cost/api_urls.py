from django.urls import path

from Cost.views import NewCostView, DeleteCostView, GetUserCostByDateView

urlpatterns = {
    path('new_cost', NewCostView.as_view()),
    path('delete_cost', DeleteCostView.as_view()),
    path('get_user_cost_by_date', GetUserCostByDateView.as_view()),
}