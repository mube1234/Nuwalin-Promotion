# Generated by Django 3.0.3 on 2020-10-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0006_auto_20201019_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
