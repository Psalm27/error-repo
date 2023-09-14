from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Docs
from .forms import DocsForm


@login_required(login_url='accounts:login_url')
def upload_docs(request):
    if request.method == 'POST':
        form = DocsForm(request.POST, request.FILES)
        if form.is_valid():
            docs = form.save(commit=False)
            docs.student = request.user
            docs.save()
            return redirect('accounts:student_profile')  # Redirect to a success page
    else:
        form = DocsForm()

    return render(request, 'doc/upload_docs.html', {'form': form})


# @login_required(login_url='accounts:login_url')
def list_cvs(request):
    cvs = Docs.objects.filter(student=request.user, cv__isnull=False).order_by('created_at')
    num = cvs.count()

    context = {
        'cvs': cvs,
        'num': num,
    }
    print(cvs, num)
    return render(request, 'doc/list_cvs.html', context)


@login_required(login_url='accounts:login_url')
def list_cover(request):
    cover_letters = Docs.objects.filter(student=request.user, cover_letter__isnull=False)
    num_cover_letters = Docs.objects.filter(cover_letter__isnull=False).count()

    context = {
        'cover_letters': cover_letters,
        'num_cover_letters': num_cover_letters,
    }
    print(cover_letters, num_cover_letters)
    return render(request, 'doc/list_cls.html', context)
