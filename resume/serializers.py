from rest_framework import serializers
from .models import PersonalInfo, ExperienceInfo

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceInfo
        fields  = '__all__'