from django.shortcuts import get_object_or_404
from api.serializers import studentSerializer,teamSerializer,UserSerializer
from api.models import Student,Team,User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Max
from rest_framework import generics,status,viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate,get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class getStudentList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Student.objects.all()
    serializer_class=studentSerializer



class getTeamList(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Team.objects.all()
    serializer_class=teamSerializer
    


class getStudentDetail(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Student.objects.all()
    serializer_class=studentSerializer
    lookup_field='enrollment_no'



class createUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

     
class loginView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')

        user=authenticate(email=email,password=password)
        if user:
            refresh = RefreshToken.for_user(user)

            return Response({
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            })

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )        
    

# For CRUD operations on Student model
class StudentViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Student.objects.all()
    serializer_class=studentSerializer


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=Team.objects.all()
    serializer_class=teamSerializer