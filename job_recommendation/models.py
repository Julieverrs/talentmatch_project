from django.db import models

class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills_required = models.TextField(default='Not specified')  # Added default value

    def __str__(self):
        return self.title


class ApplicantProfile(models.Model):
    name = models.CharField(max_length=100)
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
