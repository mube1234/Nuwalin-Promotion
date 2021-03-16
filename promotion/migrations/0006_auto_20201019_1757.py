# Generated by Django 3.0.3 on 2020-10-19 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promotion', '0005_auto_20201016_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='user1.png', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='SalesPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=100)),
                ('specific_area', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('contact_info', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ownerprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
