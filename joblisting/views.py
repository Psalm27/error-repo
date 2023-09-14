from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPosting
from .forms import JobPostingForm


@login_required
def create_job_posting(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job_posting = form.save(commit=False)
            job_posting.company = request.user
            job_posting.save()
            return redirect('job_posting_list')
    else:
        form = JobPostingForm()

    context = {'form': form}
    return render(request, 'jobs/create_job_posting.html', context)


def job_posting_list(request):
    job_postings = JobPosting.objects.all().order_by('posted_date') & JobPosting.objects.filter(expired=False)
    return render(request, 'jobs/job_posting_list.html', {'job_postings': job_postings})


def job_posting_detail(request, pk):
    job_posting = get_object_or_404(JobPosting, pk=pk)
    return render(request, 'jobs/job_posting_detail.html', {'job_posting': job_posting})
