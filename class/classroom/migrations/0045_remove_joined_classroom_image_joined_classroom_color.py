# Generated by Django 4.0.4 on 2022-06-21 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0044_remove_room_image_room_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joined',
            name='classroom_image',
        ),
        migrations.AddField(
            model_name='joined',
            name='classroom_color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
