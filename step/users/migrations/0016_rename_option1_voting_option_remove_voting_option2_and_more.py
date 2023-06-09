# Generated by Django 4.1 on 2023-03-23 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0015_voting_alter_fees_balance_alter_fees_paid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voting',
            old_name='option1',
            new_name='option',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='option4',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='option5',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='option6',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='option7',
        ),
        migrations.AddField(
            model_name='voting',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_voted', models.BooleanField(default=False)),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
