# Generated by Django 3.1.5 on 2021-01-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcooking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rekomend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='img/')),
                ('video', models.FileField(upload_to='vid/')),
                ('nama', models.CharField(max_length=500)),
                ('resep', models.TextField()),
                ('keterangan', models.TextField()),
            ],
        ),
    ]
