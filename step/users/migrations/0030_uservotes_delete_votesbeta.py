# Generated by Django 4.1 on 2023-04-03 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0029_delete_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_voted', models.BooleanField(default=False)),
                ('chosen_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.voting')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='VotesBeta',
        ),
    ]
