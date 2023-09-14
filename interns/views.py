from django.shortcuts import render, redirect
from .models import Application
from .forms import ApplicationForm


def apply_for_job(request, job_id):

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            student = request.user
            application = form.save(commit=False)
            application.student = student
            application.save()

            return redirect('job_list')

    else:
        form = ApplicationForm()

    context = {
        'form': form,
    }
    return render(request, 'apply_for_job.html', context)
