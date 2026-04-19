from django.shortcuts import get_object_or_404
from start.serializers import studentSerializer,teamSerializer
from start.models import student,team
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max
from rest_framework import generics

# Create your views here.
class getStudentList(generics.ListAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

class getTeamList(generics.ListAPIView):
    queryset=team.objects.all()
    serializer_class=teamSerializer
    
class getStudentDetail(generics.RetrieveAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer
    lookup_field='enrollment_no'
