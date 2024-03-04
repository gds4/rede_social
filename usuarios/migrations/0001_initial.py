# Generated by Django 5.0 on 2024-01-25 13:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('bio', models.TextField(max_length=240)),
                ('gender', models.CharField(choices=[('MS', 'masculino'), ('FM', 'feminino'), ('OT', 'outro')], max_length=10)),
                ('nickname', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]