from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView

from vacancy.forms import VacancyCreationForm
from resume.forms import ResumeCreationForm

class Main(View):

    def get(self, request):

        return render(request, 'main/main.html')


class LoginPage(LoginView):
    redirect_authenticated_user = True
    form_class = AuthenticationForm
    template_name = 'main/login.html'


class SignUpPage(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'main/signup.html'

    
class Profile(View):
    
    def get(self, request):

        if request.user.is_authenticated:
            if request.user.is_staff:
                form = VacancyCreationForm()
            else:
                form = ResumeCreationForm()
            return render(request, 'main/profile.html', {'form':form})
        return redirect('/')