from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, Firstname, Lastname, Username, Phone_Number, password=None,  password2=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            Firstname = Firstname,
            Lastname = Lastname,
            Username = Username,
            Phone_Number = Phone_Number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, Firstname, Lastname, Username, Phone_Number, password=None):
        user = self.create_user(
            email,
            Firstname = Firstname,
            Lastname = Lastname,
            Username = Username,
            Phone_Number = Phone_Number,
            password=password,
        )
        user.is_admin = True
        user.is_login = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address",max_length=255, unique=True)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_login = models.BooleanField(default=False)
    is_logout = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['Firstname','Lastname','Username','Phone_Number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin