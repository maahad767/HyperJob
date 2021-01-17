from django.forms.models import ModelForm

from vacancy.models import Vacancy


class VacancyCreationForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['description']

