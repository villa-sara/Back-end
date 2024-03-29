from django.conf import settings
from django.db import models
from dynamic_filenames import FilePattern
profile_image_pattern = FilePattern(filename_pattern='images/{username:.30}{ext}')


class Tenant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name="نام")
    # last_name = models.CharField(max_length=64, null=False, blank=False, verbose_name="نام خانوادگی")

    # username = models.CharField(max_length=32, null=False, blank=False, unique=True, verbose_name="نام کاربری")
    # password = models.CharField(max_length=32, null=False, blank=False, verbose_name="رمز ورود")

    # email = models.EmailField(unique=True, null=False, blank=False, verbose_name='ایمیل')
    # phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True, verbose_name="تلفن همراه")

    created_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="زمان آخرین به روزرسانی")
    profile_image = models.ImageField(upload_to=profile_image_pattern, blank=True)
    profile_image_txt = models.TextField(blank=True, verbose_name="تصویر ")

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری‌ها'

    def __str__(self):
        return self.user.__str__()
