# Generated by Django 3.0.3 on 2020-10-21 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0008_auto_20201021_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='adertising',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
