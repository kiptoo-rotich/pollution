# Generated by Django 3.2.5 on 2021-07-27 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('environment', '0002_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.TextField(max_length=1000)),
                ('estimate', models.CharField(max_length=3)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environment.post')),
            ],
        ),
    ]
