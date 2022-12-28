
from django.views.generic import ListView
from projects import models
from projects import serializers
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from projects.permissions import UpdateOwnProjects


class ProjectListView(ListView):
    model = models.Project
    template_name = 'projects/list.html'
    context_object_name = 'projects_list'

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProjectSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, UpdateOwnProjects]

    def get_queryset(self):
        qs = models.Project.objects.filter(user=self.request.user)
        return qs


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
