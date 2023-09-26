from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from course.models import Course
from school.models import School
from industry.models import Type


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

#ghanafjhnfdegnngpsdogods


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_student = models.BooleanField(default=False)
    is_organisation = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


LevelChoices = (
    ('1', 'level 100'),
    ('2', 'level 200'),
    ('3', 'level 300'),
    ('4', 'level 400'),
)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    index_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    level = models.IntegerField(choices=LevelChoices, help_text='your student level', default=1)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, related_name='students_course', blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.RESTRICT, related_name='students_school', blank=True, null=True)


class Organization(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text='The name of the organization')
    industry_type = models.ForeignKey(Type, on_delete=models.RESTRICT, related_name='organisation_types', blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, upload_to='organisation_logo/%Y/%m/%d/')

