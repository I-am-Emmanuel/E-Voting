# Generated by Django 4.1.3 on 2023-03-06 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_2', '0005_alter_election_citizen_nin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='citizen_nin',
            field=models.OneToOneField(default='00000000000', on_delete=django.db.models.deletion.CASCADE, to='core_2.verification'),
        ),
    ]
