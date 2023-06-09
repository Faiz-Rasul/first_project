# Generated by Django 4.1 on 2023-03-17 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0012_availablecourses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course1', models.CharField(blank=True, max_length=20)),
                ('course2', models.CharField(blank=True, max_length=20)),
                ('course3', models.CharField(blank=True, max_length=20)),
                ('course4', models.CharField(blank=True, max_length=20)),
                ('course5', models.CharField(blank=True, max_length=20)),
                ('course6', models.CharField(blank=True, max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
