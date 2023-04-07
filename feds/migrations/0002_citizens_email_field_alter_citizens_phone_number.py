# Generated by Django 4.1.3 on 2023-02-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizens',
            name='email_field',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='citizens',
            name='phone_number',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
