from django.contrib import admin

from vacancy.models import Vacancy
from resume.models import Resume

admin.site.register(Vacancy)
admin.site.register(Resume)