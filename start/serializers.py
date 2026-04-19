from rest_framework import serializers
from .models import student,team

class studentSerializer(serializers.ModelSerializer):
    team_name=serializers.CharField(source='team.team_name',read_only=True)
    class Meta:
        model=student
        fields=(
            'enrollment_no',
            'name',
            'age',
            'team_name',
        )

class teamSerializer(serializers.ModelSerializer):
    class Meta:
        model=team
        fields=(
            'team_id',
            'team_name',
        )
