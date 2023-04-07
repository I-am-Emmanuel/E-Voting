# Generated by Django 4.1.3 on 2023-03-04 05:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feds', '0008_rename_email_field_citizens_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nin', models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11, message='Your NIN should be 11 digit numbers'), django.core.validators.MaxLengthValidator(11)])),
                ('birth_date', models.DateField()),
                ('other_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='citizen_detail', to='feds.citizens')),
            ],
        ),
    ]