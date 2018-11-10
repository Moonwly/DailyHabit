from django.urls import path

from Goal.views import NewGoalView, FinishGoalView, RestartGoalView, DeleteGoalView, ModifyGoalView, \
    GetUserGoalByIDView, GetGoalByUserView, GetUserGoalsByGoalStatusView, GetUserTodayGoalsView

urlpatterns = {
    path('new_goal', NewGoalView.as_view()),
    path('finish_goal', FinishGoalView.as_view()),
    path('restart_goal', RestartGoalView.as_view()),
    path('delete_goal', DeleteGoalView.as_view()),
    path('modify_goal', ModifyGoalView.as_view()),
    path('get_user_goal_by_id', GetUserGoalByIDView.as_view()),
    path('get_goal_by_user', GetGoalByUserView.as_view()),
    path('get_user_goal_by_goal_status', GetUserGoalsByGoalStatusView.as_view()),
    path('get_user_today_goals', GetUserTodayGoalsView.as_view()),
}