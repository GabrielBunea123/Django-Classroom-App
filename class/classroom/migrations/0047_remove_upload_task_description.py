# Generated by Django 4.0.4 on 2022-06-22 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0046_upload_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload_task',
            name='description',
        ),
    ]