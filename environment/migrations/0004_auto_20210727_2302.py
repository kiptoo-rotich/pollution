# Generated by Django 3.2.5 on 2021-07-27 23:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0003_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cleanup',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
