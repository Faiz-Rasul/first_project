# Generated by Django 4.1 on 2023-03-15 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_otherrequests_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherrequests',
            name='response',
            field=models.CharField(default='Response Pending', max_length=150),
        ),
    ]
