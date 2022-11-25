from django.contrib import admin
from .models import User, SurveyResponse, Story

admin.site.register(User)
admin.site.register(SurveyResponse)
admin.site.register(Story)