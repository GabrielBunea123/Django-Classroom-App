# Generated by Django 3.2.4 on 2021-06-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_joined_classroom_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='joined',
            name='classroom_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
