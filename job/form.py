from django import forms
from .models import Apply, Job

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = [
            'name',
            'email',
            'website',
            'cv',
            'cover_letter',
        ]
class JobForm(forms.ModelForm):
    class Meta:
        model =Job
        fields = [
            'category',
            'title',
            'job_type',
            'description',
            'vacancy',
            'salary',
            'experience',
            'image',
            
        ]