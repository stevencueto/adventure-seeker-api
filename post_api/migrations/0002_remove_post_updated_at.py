# Generated by Django 4.0.3 on 2022-04-18 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]
