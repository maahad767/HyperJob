from django.forms.models import ModelForm

from resume.models import Resume


class ResumeCreationForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['description']
