from .models import Job
from rest_framework import viewsets, permissions
from .serializers import JobSerializer


# Views
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]

