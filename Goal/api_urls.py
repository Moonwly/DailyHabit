from django.urls import path

from Goal.views import NewGoalView, FinishGoalView, RestartGoalView, DeleteGoalView, ModifyGoalView, \
    GetUserGoalByIDView, GetGoalByUser, GetUserGoalsByGoalStatus

urlpatterns = {
    path('new_goal', NewGoalView.as_view()),
    path('finish_goal', FinishGoalView.as_view()),
    path('restart_goal', RestartGoalView.as_view()),
    path('delete_goal', DeleteGoalView.as_view()),
    path('modify_goal', ModifyGoalView.as_view()),
    path('get_user_goal_by_id', GetUserGoalByIDView.as_view()),
    path('get_goal_by_user', GetGoalByUser.as_view()),
    path('get_user_goal_by_goal_status', GetUserGoalsByGoalStatus.as_view()),
}