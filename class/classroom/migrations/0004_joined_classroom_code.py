# Generated by Django 3.2.4 on 2021-06-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='joined',
            name='classroom_code',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
