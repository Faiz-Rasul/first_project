# Generated by Django 4.1 on 2023-03-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_rename_option1_voting_option_remove_voting_option2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='option',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]
