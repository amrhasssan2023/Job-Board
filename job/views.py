from django.shortcuts import render, redirect
from .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm, JobForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def job_list(request):
    add_job = Job.objects.filter(active=True).count()

    job_list = Job.objects.all()
    paginator = Paginator(job_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {
        'jobs' : page_obj,
        'add_jobs' : add_job,
    }

    return render(request,'pages/jobs.html', context)

def job_details(request, slug):
    job_details = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.job = job_details
            myform.save()
            
    else:
        form = ApplyForm()



    context = {
        'job' : job_details,
        'form' : form
    }
    return render(request, 'pages/job_details.html',context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form1 = JobForm(request.POST, request.FILES)
        if form1.is_valid():
            myform = form1.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect('/')
    else:
        form1 = JobForm()

    context = {
        'form1' : form1
    }
    return render(request, 'pages/add_job.html', context)