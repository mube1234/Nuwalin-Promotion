# Generated by Django 3.0.3 on 2020-10-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0017_auto_20201027_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_news',
            name='type',
            field=models.CharField(blank=True, choices=[('news', 'news'), ('entertainment', 'entertainment')], max_length=100, null=True),
        ),
    ]
