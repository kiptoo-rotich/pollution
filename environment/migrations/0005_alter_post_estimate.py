# Generated by Django 3.2.5 on 2021-07-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0004_auto_20210727_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='estimate',
            field=models.CharField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0, max_length=10),
        ),
    ]