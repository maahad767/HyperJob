from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseForbidden

from vacancy.models import Vacancy
from vacancy.forms import VacancyCreationForm

class Vacancies(View):

    def get(self, request):
        vacancy_list = Vacancy.objects.all()
        context = {
            'vacancies': vacancy_list,
        }
        return render(request, 'vacancy/vacancies.html', context=context)


class CreateVacancy(View):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            form = VacancyCreationForm(request.POST)
            if form.is_valid():
                vacancy = form.save(commit=False)
                vacancy.author = request.user
                vacancy.save()
                return redirect('profile')
        return HttpResponseForbidden()
