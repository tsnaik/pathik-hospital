# Generated by Django 2.2.2 on 2019-06-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=1000)),
                ('address2', models.CharField(blank=True, max_length=1000, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(default='India', max_length=15)),
                ('zip_code', models.CharField(blank=True, max_length=15, null=True)),
                ('dob', models.DateField()),
                ('age', models.PositiveSmallIntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=2)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=5, null=True)),
                ('remarks', models.TextField()),
                ('date_of_registration', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
