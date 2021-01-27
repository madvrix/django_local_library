# Generated by Django 3.1.5 on 2021-01-22 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tcooking', '0002_rekomend'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='img/')),
                ('video', models.FileField(upload_to='vid/')),
                ('nama', models.CharField(max_length=500)),
                ('resep', models.TextField()),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=200, null=True)),
                ('nodata', models.IntegerField(null=True)),
                ('norole', models.CharField(choices=[('2', 'Vendor'), ('3', 'Client')], max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
