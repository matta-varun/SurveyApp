from django.contrib.auth.models import AbstractUser
from django.db import models

class Story(models.Model):
    photo_filename = models.CharField( max_length=128, null=False, blank=True )
    story_id = models.IntegerField( default = 0, null=False, blank=False, unique = True )
    explanation_link = models.CharField(max_length=512)
    summary = models.TextField()

class SurveyResponse(models.Model):
    story_1 = models.ForeignKey(Story, blank=True, null=True, related_name="story_1", on_delete=models.CASCADE)
    response_1 = models.SmallIntegerField(default=-100, null=True)
    seen_before_1 = models.CharField(max_length=256, null=True, blank=True)
    story_2 = models.ForeignKey(Story, blank=True, null=True, related_name="story_2", on_delete=models.CASCADE)
    response_2 = models.SmallIntegerField(default=-100)
    seen_before_3 = models.CharField(max_length=256, null=True, blank=True)
    story_3 = models.ForeignKey(Story, blank=True, null=True, related_name="story_3", on_delete=models.CASCADE)
    response_3 = models.SmallIntegerField(default=-100)
    seen_before_3 = models.CharField(max_length=256, null=True, blank=True)
    

class User(AbstractUser):
    '''
    '''
    
    username = models.CharField(max_length=64, primary_key = True, unique = True)
    consent_status = models.BooleanField(default = False)
    questions_answered = models.SmallIntegerField(default=0, unique=False, blank=False)
    survey_response = models.ForeignKey(SurveyResponse, blank=True, null=True, on_delete=models.CASCADE)
    age_group = models.CharField(max_length=100, null=True, unique=False)
    gender = models.CharField(max_length=100, null=True, unique=False)
    education = models.CharField(max_length=100, null=True, unique=False)
    social_media_usage = models.CharField(max_length=256, null=True, blank=True)