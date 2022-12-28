from rest_framework import serializers
from projects import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('id', 'name', 'user', 'status', 'created_at', 'updated_at')
        extra_kwargs = {
            'user': {
                'read_only': True,
            },
            'status': {
                'default': True
            }
        }
