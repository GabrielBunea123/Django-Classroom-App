# Generated by Django 3.2.4 on 2021-06-30 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0033_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_task',
            name='topic',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]