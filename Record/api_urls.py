from django.urls import path

from Record.views import NewRecordView, CancelRecordView, GetUserRecordView, GetUserRecordByDateView

urlpatterns = {
    path('new_record', NewRecordView.as_view()),
    path('cancel_record', CancelRecordView.as_view()),
    path('get_user_record', GetUserRecordView.as_view()),
    path('get_user_record_by_date', GetUserRecordByDateView.as_view()),
}