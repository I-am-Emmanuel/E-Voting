# Generated by Django 4.1.3 on 2023-03-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_usermodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='otp',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
