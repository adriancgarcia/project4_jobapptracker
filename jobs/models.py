from django.db import models

# models
class Job(models.Model):
    position = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=200)
    applied = models.BooleanField()
    type_of_resume_sent = models.CharField(max_length=200)
    date_applied = models.DateField()
    hiring_manager = models.CharField(max_length=200)
    hiring_manager_email = models.CharField(max_length=200)
    hiring_manager_phone = models.IntegerField()
    interview_status = models.CharField(max_length=200)
    application_origin = models.CharField(max_length=200)
    thankyou_sent = models.BooleanField()

