from django.urls import path
from projects.views import *
urlpatterns = [
    path('list/', ProjectListView.as_view()),
]