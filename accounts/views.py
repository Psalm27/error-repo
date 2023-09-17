import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Organization, CustomUser
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages, auth
from .forms import LoginForm, StudentRegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required


#
#
# # Create your views here.
#
@login_required(login_url='accounts:login_url')
@permission_required('can_view_student_profile', raise_exception=True)
def student_profile(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if not request.user.is_staff and not request.user == student:
        raise PermissionDenied("You do not have permission to view this student's profile.")
    context = {'student': student}
    return render(request, 'student/student_profile.html', context)


#
#
# @login_required(login_url='accounts:login_url')
# @permission_required('can_view_organisation_profile', raise_exception=True)
# def organisation_profile(request, organisation_id):
#     organise = get_object_or_404(Organization, pk=organisation_id)
#     if not request.user.is_staff and not request.user == organise:
#         raise PermissionDenied("You do not have permission to view this student's profile.")
#     context = {'organise': organise}
#     return render(request, 'organisation/organis_profile.html', context)
#
#
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_student:
                return redirect('accounts:student_profile', student_id=user.student.id)
            elif user.is_organization:
                return redirect('accounts:organization_profile', organization_id=user.organization.id)
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')


@login_required(login_url='accounts:login_url')
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('accounts:login_url')


#
#
@login_required(login_url='accounts:login_url')
def activate(request, user_type, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        User = get_user_model()

        if user_type == 'student':
            user = User.objects.get(pk=uid, is_student=True)
        elif user_type == 'organization':
            user = User.objects.get(pk=uid, is_organization=True)
        else:
            user = None

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('accounts:login_url')
    else:
        messages.error(request, 'Invalid activation link.')
        return redirect('register')


#
def register_student(request):
    ip_address = request.META.get('REMOTE_ADDR')
    timestamp = datetime.datetime.now()

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            user = CustomUser.objects.create_user(
                email=email,
                password=form.cleaned_data['password'],
                is_student=True
            )
            student = Student.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                index_number=form.cleaned_data['index_number'],
                course=form.cleaned_data['course'],
                level=form.cleaned_data['level'],
                school=form.cleaned_data['school'],
            )

            # Sending email for verification
            current_site = get_current_site(request)
            mail_subject = "Account Activation"
            message = render_to_string('verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Sign up was successful. Please complete your verification from your email.')
            return redirect('/accounts/login/?command=verification&email=' + email)
    else:
        form = StudentRegistrationForm()

    context = {
        "form": form,
        'ip_address': ip_address,
        'timestamp': timestamp,
    }

    return render(request, 'signup.html', context)
#
#
# # def register_staff(request):
# #     ip_address = request.META.get('REMOTE_ADDR')
# #     timestamp = datetime.datetime.now()
# #     if request.method == 'POST':
# #         form = OrganizationRegistrationForm(request.POST)
# #         if form.is_valid():
# #             name = form.cleaned_data['name']
# #             email = form.cleaned_data['email']
# #             industry_type = form.cleaned_data['industry_type']
# #             logo = form.cleaned_data['logo']
# #             password = form.cleaned_data['password']
# #             user = Organization.objects.create_user(name=name, industry_type=industry_type,
# #                                                     logo=logo, email=email,
# #                                                     password=password)
# #             user.save()
# #             # making my user activation
# #             if 'next' in request.POST:
# #                 return redirect(request.POST.get('next'))
# #
# #             current_site = get_current_site(request)
# #             mail_subject = "Accounts Activation"
# #             message = render_to_string('verification.html', {
# #                 'user': user,
# #                 'domain': current_site,
# #                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
# #                 'token': default_token_generator.make_token(user),
# #             })
# #
# #             to_email = email
# #             send_email = EmailMessage(mail_subject, message, to=[to_email])
# #             send_email.send()
# #             messages.success(request, 'Sign up was successful, please complete your verification from your mail')
# #             return redirect('/accounts/login/?command=verification&email=' + email)
# #     else:
# #         form = OrganizationRegistrationForm()
# #     context = {
# #         "form": form,
# #         'ip_address': ip_address,
# #         'timestamp': timestamp,
# #     }
# #     print(ip_address, timestamp)
# #     return render(request, 'organisationsignup.html', context)
#

def forgetpassword(request):
    ip_address = request.META.get('REMOTE_ADDR')
    timestamp = datetime.datetime.now()

    if request.method == 'POST':
        email = request.POST.get('email')

        student = Student.objects.filter(email=email).first()
        organization = Organization.objects.filter(email=email).first()

        if student or organization:
            user = student if student else organization

            current_site = get_current_site(request)
            mail_subject = "Accounts Reset"
            context = {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'ip_address': ip_address,
                'timestamp': timestamp,
            }
            message = render_to_string('reset_verification.html', context)

            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, "Password reset email has been sent to your email")
            return redirect('accounts:login_url')
        else:
            messages.error(request, "No user with that email address exists.")
            return redirect('accounts:login_url')

    context = {
        'ip_address': ip_address,
        'timestamp': timestamp,
    }
    print(ip_address)
    return render(request, 'forgotpassword.html', context)


#
def resetpassword_validate(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()
    user = get_object_or_404(CustomUser, pk=uid)

    if default_token_generator.check_token(user, token):
        if hasattr(user, 'student'):
            request.session['uid'] = uid
            messages.success(request, 'Please reset your student password.')
            return redirect('accounts:reset_student_password_url')
        elif hasattr(user, 'organization'):
            request.session['uid'] = uid
            messages.success(request, 'Please reset your organization password.')
            return redirect('accounts:reset_organization_password_url')
    else:
        messages.error(request, 'This link has expired.')
        return redirect('accounts:resetpassword_url')


def resetpassword_student(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Student.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password Reset Was Successful')
            return redirect('accounts:login_url')
        else:
            messages.error(request, "passwords dont match")
            return redirect('accounts:reset_student_password_url')
    else:
        return render(request, 'resetpass.html')


def resetpassword_organ(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Organization.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password Reset Was Successful')
            return redirect('accounts:login_url')
        else:
            messages.error(request, "passwords dont match")
            return redirect('accounts:reset_organization_password_url')
    else:
        return render(request, 'orgresetpass.html')
