from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import User, SurveyResponse, Story
from .forms import ConsentForm, ExplainabilityForm, SurveyForm
import random
import string

story_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
explainability_map = {
    "No, the post appears to be true" : -2,
    "The post looks like it is mostly true" : -1,
    "I am not sure about this post" : 0,
    "The post looks like it is mostly false" : 1,
    "Yes, the post appears to be spreading false information" : 2
}

seen_before_map = {
    'I was aware of this post and knew it was misinformed / not-misinformed beforehand' : 1,
    'I was aware of this post but did not know it was misinformed / not-misinformed beforehand' : -1,
    'No, I was not aware of this post beforehand' : -2,
    'I am not sure' : 0
}


def homepage(request):
    if request.user.is_authenticated:
        return redirect('survey')
    else:
        return render(request, 'homepage.html')

def privacy(request):
    return render(request, 'privacy.html')

def consent(request):
    if request.user.is_authenticated:
        return redirect('survey')
    else:
        if request.method == 'POST':
            form = ConsentForm(data = request.POST)
            
            if form.is_valid():
                if form.cleaned_data['consent_status'] == 'Yes, I consent':
                    user = User.objects.create(username = 'User' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10)))
                    user.consent_status = True
                    # user.save()
                    survey = SurveyResponse.objects.create()
                    survey.save()
                    user.survey_response = survey
                    user.consent_status = True
                    user.save()
                    story_list = random.sample(story_ids, 3)
                    survey.story_1 = Story.objects.get(story_id = story_list[0])
                    survey.story_2 = Story.objects.get(story_id = story_list[1])
                    survey.story_3 = Story.objects.get(story_id = story_list[2])
                    survey.save()
                    
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    
                    return redirect('survey')                    
                else:
                    return render(request, 'text-template.html', {"text" : "We understand, have a great day ahead!"})
        else:
            form = ConsentForm()
        
        return render(request, 'consent.html', {'form' : form})

def survey(request):
    if request.user.is_authenticated:
        
        if request.user.questions_answered == 0:
            
            filename = "/static/" + request.user.survey_response.story_1.photo_filename
            link = request.user.survey_response.story_1.explanation_link
            summary = request.user.survey_response.story_1.summary
            question_no = 1
            
            if request.method == 'POST':
                form = ExplainabilityForm(data = request.POST)
                
                if form.is_valid():
                    if form.cleaned_data['misinformation_degree'] in explainability_map.keys():
                        survey_response = request.user.survey_response
                        user = User.objects.get(username = request.user.username)
                        survey_response.response_1 = explainability_map[form.cleaned_data['misinformation_degree']]
                        survey_response.seen_before_1 = seen_before_map[form.cleaned_data['seen_before']]
                        survey_response.save()
                        user.questions_answered += 1
                        user.save()
                        
                        filename = "/static/" + request.user.survey_response.story_2.photo_filename
                        link = request.user.survey_response.story_2.explanation_link
                        summary = request.user.survey_response.story_2.summary
                        form = ExplainabilityForm()
                        question_no = 2
                        
                        return render(request, 'survey.html', {'form' : form, 'photo_filename' : filename, 'question_no' : question_no, 'link' : link, 'summary' : summary})
            else:
                form = ExplainabilityForm()
            
            return render(request, 'survey.html', {'form' : form, 'photo_filename' : filename, 'question_no' : question_no, 'link' : link, 'summary' : summary})
        
        elif request.user.questions_answered == 1:
            
            filename = "/static/" + request.user.survey_response.story_2.photo_filename
            link = request.user.survey_response.story_2.explanation_link
            summary = request.user.survey_response.story_2.summary
            question_no = 2
            
            if request.method == 'POST':
                form = ExplainabilityForm(data = request.POST)
                
                if form.is_valid():
                    if form.cleaned_data['misinformation_degree'] in explainability_map.keys():
                        survey_response = request.user.survey_response
                        user = User.objects.get(username = request.user.username)
                        survey_response.response_2 = explainability_map[form.cleaned_data['misinformation_degree']]
                        survey_response.seen_before_2 = seen_before_map[form.cleaned_data['seen_before']]
                        survey_response.save()
                        user.questions_answered += 1
                        user.save()
                        
                        filename = "/static/" + request.user.survey_response.story_3.photo_filename
                        link = request.user.survey_response.story_3.explanation_link
                        summary = request.user.survey_response.story_3.summary
                        form = ExplainabilityForm()
                        question_no = 3
                        
                        return render(request, 'survey.html', {'form' : form, 'photo_filename' : filename, 'question_no' : question_no, 'link' : link, 'summary' : summary})
            else:
                form = ExplainabilityForm()
            
            return render(request, 'survey.html', {'form' : form, 'photo_filename' : filename, 'question_no' : question_no, 'link' : link, 'summary' : summary})
            
        elif request.user.questions_answered == 2:
            
            filename = "/static/" + request.user.survey_response.story_3.photo_filename
            link = request.user.survey_response.story_3.explanation_link
            summary = request.user.survey_response.story_3.summary
            question_no = 3
            
            if request.method == 'POST':
                form = ExplainabilityForm(data = request.POST)
                
                if form.is_valid():
                    if form.cleaned_data['misinformation_degree'] in explainability_map.keys():
                        survey_response = request.user.survey_response
                        user = User.objects.get(username = request.user.username)
                        survey_response.response_3 = explainability_map[form.cleaned_data['misinformation_degree']]
                        survey_response.seen_before_3 = seen_before_map[form.cleaned_data['seen_before']]
                        survey_response.save()
                        user.questions_answered += 1
                        user.save()
                        
                        form = SurveyForm()
                        question_no = 4
                        
                        return render(request, 'survey.html', {'form' : form, 'photo_filename' : filename, 'question_no' : question_no, 'link' : link, 'summary' : summary})
            else:
                form = ExplainabilityForm()
            
            return render(request, 'survey.html', {'form' : form, 'photo_filename' : filename, 'question_no' : question_no, 'link' : link, 'summary' : summary})
            
        elif request.user.questions_answered == 3:
            question_no = 4
            filename = "/static/" + request.user.survey_response.story_3.photo_filename
            link = request.user.survey_response.story_3.explanation_link
            summary = request.user.survey_response.story_3.summary
            
            if request.method == 'POST':
                form = SurveyForm(data = request.POST)
                
                if form.is_valid():
                    # survey_response = request.user.survey_response
                    user = User.objects.get(username = request.user.username)
                    user.age_group = form.cleaned_data['agegroup']
                    user.gender = form.cleaned_data['gender']
                    user.education = form.cleaned_data['education']
                    user.social_media_usage = form.cleaned_data['social_media_usage']
                    user.questions_answered += 1
                    user.save()
                        
                    return redirect('dashboard')
            else:
                form = SurveyForm()
            
            return render(request, 'survey.html', {'form' : form, 'photo_filename' : filename, 'question_no' : question_no, 'link' : link, 'summary' : summary})
        else:
            return redirect('dashboard')
    else:
        return redirect('consent')

def dashboard(request):
    
    if request.user.is_authenticated:
        if request.user.questions_answered == 4:
            survey_response = request.user.survey_response
            story_1 = "/static/" + survey_response.story_1.photo_filename
            link_1 = survey_response.story_1.explanation_link
            summary_1 = survey_response.story_1.summary
            story_2 = "/static/" + survey_response.story_2.photo_filename
            link_2 = survey_response.story_2.explanation_link
            summary_2 = survey_response.story_2.summary
            story_3 = "/static/" + survey_response.story_3.photo_filename
            link_3 = survey_response.story_3.explanation_link
            summary_3 = survey_response.story_3.summary
            
            return render(request, 'thank-you.html', {
                'story_1' : story_1, 
                'link_1' : link_1, 
                'summary_1' : summary_1,
                'story_2' : story_2, 
                'link_2' : link_2, 
                'summary_2' : summary_2,
                'story_3' : story_3, 
                'link_3' : link_3,
                'summary_3' : summary_3}
                          )
            
        else:
            return redirect('survey')
    else:
        return redirect('consent')


def delete_my_data(request):
    
    if request.user.is_authenticated:
        user = request.user
        survey_response = user.survey_response
        survey_response.delete()
        user.delete()
        logout(request)
        return render(request, 'text-template.html', {'text' : 'Your data has been successfully deleted!'})
    else:
        return redirect('consent')