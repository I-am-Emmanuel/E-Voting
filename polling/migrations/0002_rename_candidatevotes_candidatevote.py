# Generated by Django 4.1.3 on 2023-04-18 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CandidateVotes',
            new_name='CandidateVote',
        ),
    ]