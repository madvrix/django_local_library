# Generated by Django 3.1.5 on 2021-01-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
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
