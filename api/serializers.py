from rest_framework import serializers
from .models import Student,Team,User

class studentSerializer(serializers.ModelSerializer):
    team_name=serializers.CharField(source='team.team_name',read_only=True)
    class Meta:
        model=Student
        fields=(
            'enrollment_no',
            'name',
            'age',
            'team_name',
        )

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=(
            'team_id',
            'team_name',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': False}
        }
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user