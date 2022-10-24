from django.contrib import admin
from .models import Candidate

# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'position', 'votes')

admin.site.register(Candidate, CandidateAdmin)
