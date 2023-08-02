from django.contrib import admin
from .models import Category, Job , Apply
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'job_type',
        'description',
        'published_at',
        'vacancy',
        'salary',
        'experience',
        'category',
        'active',
    ]
    search_fields = ['title']
    list_filter = ['title', 'category']

admin.site.register(Category)
admin.site.register(Job, JobAdmin)
admin.site.register(Apply)
