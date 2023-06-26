from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('guest', 'مهمان'),
        ('host', 'میزبان'),
    )
    username = models.CharField(max_length=15, null=False, blank=False, unique=True, verbose_name="تلفن همراه")
    # phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True, verbose_name="تلفن همراه")
    # first_name = models.CharField(max_length=32, null=False, blank=False, verbose_name="نام")
    # last_name = models.CharField(max_length=64, null=False, blank=False, verbose_name="نام خانوادگی")
    # password = models.CharField(max_length=32, null=False, blank=False, verbose_name="رمز ورود")
    # email = models.EmailField(blank=False, null=False, verbose_name='ایمیل')
    national_code = models.CharField(max_length=10, null=True, blank=False, verbose_name='کد ملی')
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="زمان ثبت")
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="زمان آخرین به روزرسانی")
    # profile_image = models.ImageField(upload_to=profile_image_pattern, blank=True)
    # REQUIRED_FIELDS = ['phone_number']
    image = []
    role = models.CharField(max_length=20, choices=ROLES, null=True, verbose_name='نقش')
    # USERNAME_FIELD = 'phone_number'

    class Meta:
        verbose_name = 'کاربر پایه'
        verbose_name_plural = 'کاربران پایه'

    def __str__(self):
        return self.username

    def check_role(self, raw_role):
        if self.role == raw_role:
            return True
        elif self.role != raw_role:
            return False
