# Generated by Django 4.1.3 on 2023-02-27 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feds', '0003_alter_citizens_email_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizens',
            name='nin',
            field=models.IntegerField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(11, message='Your NIN should be 11 digit numbers')]),
        ),
        migrations.AlterField(
            model_name='citizens',
            name='phone_number',
            field=models.CharField(max_length=14),
        ),
    ]