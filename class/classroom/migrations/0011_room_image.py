# Generated by Django 3.2.4 on 2021-06-15 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0010_alter_upload_task_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(null=True, upload_to='room_images/'),
        ),
    ]
