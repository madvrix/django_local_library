# Generated by Django 3.1.5 on 2021-01-25 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcooking', '0005_favorit_no_fav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorit',
            name='no_fav',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
