from django.db import models


# Create your models here.

class Patient(models.Model):
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    # name
    first_name = models.CharField(max_length=50, db_index=True)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # address
    address1 = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=15, default='India')
    zip_code = models.CharField(max_length=15, blank=True, null=True)

    dob = models.DateField()
    age = models.PositiveSmallIntegerField()

    # sex
    M = 'M'
    F = 'F'
    O = 'O'
    SEX_CHOICES = [
        (M, 'Male'),
        (F, 'Female'),
        (O, 'Other'),
    ]
    sex = models.CharField(
        max_length=2,
        choices=SEX_CHOICES,
        default=M,
    )

    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, blank=True, null=True)

    blood_group = models.CharField(max_length=5, blank=True, null=True)
    remarks = models.TextField()

    date_of_registration = models.DateTimeField(auto_now_add=True)

    # TODO add file column
