# Generated by Django 3.2.4 on 2021-06-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0011_room_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='joined',
            name='classroom_image',
            field=models.ImageField(null=True, upload_to='room_images/'),
        ),
    ]
