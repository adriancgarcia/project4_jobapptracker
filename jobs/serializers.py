from .models import Job
from rest_framework import serializers

# Job Serializer
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('id','position', 'company_name', 'job_description', 'applied', 'type_of_resume_sent', 'date_applied', 'hiring_manager', 'hiring_manager_email', 'hiring_manager_phone', 'interview_status', 'application_origin', 'thankyou_sent')