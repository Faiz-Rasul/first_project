# Generated by Django 4.1 on 2023-03-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_fees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.CharField(blank=True, max_length=35)),
                ('option2', models.CharField(blank=True, max_length=35)),
                ('option3', models.CharField(blank=True, max_length=35)),
                ('option4', models.CharField(blank=True, max_length=35)),
                ('option5', models.CharField(blank=True, max_length=35)),
                ('option6', models.CharField(blank=True, max_length=35)),
                ('option7', models.CharField(blank=True, max_length=35)),
            ],
        ),
        migrations.AlterField(
            model_name='fees',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fees',
            name='paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fees',
            name='penalty',
            field=models.IntegerField(default=0),
        ),
    ]
