# Generated by Django 4.1.3 on 2023-03-07 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_2', '0007_alter_presidentialcandidate_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='citizen_nin',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11, message='Your NIN should be 11 digit numbers'), django.core.validators.MaxLengthValidator(11)]),
        ),
    ]
