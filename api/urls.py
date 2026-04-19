from django.urls import path
from . import views

urlpatterns=[
    path('students/',views.getStudentList.as_view()),
    path('teams/',views.getTeamList.as_view()),
    path('students/<int:enrollment_no>',views.getStudentDetail.as_view()),
    path('create-user/',views.createUserView.as_view()),
    path('login/',views.loginView.as_view())
]