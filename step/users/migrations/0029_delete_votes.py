# Generated by Django 4.1 on 2023-04-03 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_alter_votesbeta_voter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Votes',
        ),
    ]