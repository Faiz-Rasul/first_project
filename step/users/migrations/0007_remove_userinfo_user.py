# Generated by Django 4.1 on 2023-03-15 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_user_id_userinfo_user_for'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
    ]