# Generated by Django 3.0.3 on 2020-10-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0004_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
