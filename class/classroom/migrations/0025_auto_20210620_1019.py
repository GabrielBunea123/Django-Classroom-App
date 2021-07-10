# Generated by Django 3.2.4 on 2021-06-20 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0024_alter_joined_classroom_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_task',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='upload_task',
            name='max_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
