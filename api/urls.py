from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'students',views.StudentViewSet,basename='student')
router.register(r'teams',views.TeamViewSet,basename='team')

urlpatterns = [
    path('create-user/', views.createUserView.as_view()),
    path('login/', views.loginView.as_view()),
    path('', include(router.urls)) # This handles /students/ and /teams/ correctly
]