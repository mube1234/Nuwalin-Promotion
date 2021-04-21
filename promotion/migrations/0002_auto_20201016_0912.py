# Generated by Django 3.0.3 on 2020-10-16 07:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_news',
            name='body',
            field=models.CharField(default=django.utils.timezone.now, max_length=3000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='add_news',
            name='title',
            field=models.CharField(max_length=700),
        ),
    ]