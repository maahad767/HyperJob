from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseForbidden

from resume.models import Resume
from resume.forms import ResumeCreationForm

class Resumes(View):

    def get(self, request):
        resume_list = Resume.objects.all()
        context = {
            'resumes': resume_list,
        }
        return render(request, 'resume/resumes.html', context=context)


class CreateResume(View):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = ResumeCreationForm(request.POST)
            if form.is_valid():
                resume = form.save(commit=False)
                resume.author = request.user
                resume.save()
                return redirect('profile')
        return HttpResponseForbidden()
