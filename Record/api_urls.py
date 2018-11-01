from django.urls import path

from Record.views import NewRecordView

urlpatterns = {
    path('new_record', NewRecordView.as_view()),
}