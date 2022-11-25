from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab

consent_choices = [
    ('Yes, I consent', 'Yes, I consent'),
    ('No, I do not consent', 'No, I do not consent')
]

seen_before_choices = [
    ('I was aware of this post and knew it was misinformed / not-misinformed beforehand', 'I was aware of this post and knew it was misinformed / not-misinformed beforehand'),
    ('I was aware of this post but did not know it was misinformed / not-misinformed beforehand', 'I was aware of this post but did knew it was misinformed / not-misinformed beforehand'),
    ('No, I was not aware of this post beforehand', 'No, I was not aware of this post beforehand'),
    ('I am not sure', 'I am not sure')
]

explainability_choices = [
    ('No, the post appears to be true', 'No, the post appears to be true'),
    ('The post looks like it is mostly true', 'The post looks like it is mostly true'),
    ('I am not sure about this post', 'I am not sure about this post'),
    ('The post looks like it is mostly false', 'The post looks like it is mostly false'),
    ('Yes, the post appears to be spreading false information', 'Yes, the post appears to be spreading false information')
]

class ConsentForm(forms.Form):
    consent_status = forms.ChoiceField(label="Do you consent?", choices=consent_choices, required=True, widget = forms.RadioSelect)

class ExplainabilityForm(forms.Form):
    misinformation_degree = forms.ChoiceField(label="Do you think the above post is misinformed (or) false?", choices=explainability_choices, required=True, widget = forms.RadioSelect)
    seen_before = forms.ChoiceField(label="Were you aware that the above post is certainly (misinformed)/(not misinformed) before starting this survey?", choices=seen_before_choices, required=True, widget = forms.RadioSelect)

class SurveyForm(forms.Form):
    gender_list = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say')
    ]
    
    age_groups = [
        ('18 - 20 years', '18 - 20 years'),
        ('21 - 25 years', '21 - 25 years'),
        ('26 - 30 years', '26 - 30 years'),
        ('31 - 35 years', '31 - 35 years'),
        ('36 and above', '36 and above'),
        ('Prefer not to say', 'Prefer not to say')
    ]
    
    education_list = [
        ('Middle School', 'Middle School'),
        ('High School', 'High School'),
        ('College', 'College'),
        ('Graduate', 'Graduate'),
        ('Post Graduate', 'Post Graduate'),
        ('Doctorate', 'Doctorate'),
        ('Not educated', 'Not educated'),
        ('Prefer not to say', 'Prefer not to say')
    ]
    
    usage_list = [
        ('Several times a day', 'Several times a day'),
        ('About once a day', 'About once a day'),
        ('A few times a week', 'A few times a week'),
        ('Less often', 'Less often'),
        ('Don\'t know or prefer not to say', 'Don\'t know or prefer not to say'),
        ('I don\'t use social media', 'I don\'t use social media')
    ]
    
    gender = forms.ChoiceField(label="What is your gender?", choices=gender_list, widget=forms.RadioSelect, required=True)
    agegroup = forms.ChoiceField(label="What age-group do you belong to?", choices=age_groups, widget=forms.RadioSelect, required=True)
    education = forms.ChoiceField(label="What is your highest educational qualification?", choices=education_list, widget=forms.RadioSelect, required=True)
    social_media_usage = forms.ChoiceField(label="How often do you use social media in your daily life?", choices=usage_list, widget=forms.RadioSelect, required=True)