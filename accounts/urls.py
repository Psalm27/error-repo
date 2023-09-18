from django.urls import path
from .views import student_profile, activate, register_student, login_view, \
    resetpassword_validate, forgetpassword, resetpassword_student, dashboard, resetpassword_organ

#
# #
app_name = 'accounts'
urlpatterns = [
    #     #
        path('student/<int:student_id>/', student_profile, name='student_profile'),
        path('student/', dashboard, name='student_das'),
    #     #     path('organisation/<int:organisation_id>/', organisation_profile, name='organisation_profile'),
        path('login/', login_view, name='login_url'),
        path('activate/<uidb64>/<token>/', activate, name='activate'),
        path('ssignup/', register_student, name='register_student'),
    #     #     # path('osdsignup/', register_staff, name='register_staff'),
    #     #     # password
        path('resetpasswordv/<uidb64>/<token>/', resetpassword_validate, name='reset_password_validate_url'),
        path('forgotpassword/', forgetpassword, name='forgotpassword_url'),
        path('resetstudent/', resetpassword_student, name='reset_student_password_url'),
    #     #     path('resetorganisation/', resetpassword_organ, name='reset_organization_password_url'),
    #     #
]
