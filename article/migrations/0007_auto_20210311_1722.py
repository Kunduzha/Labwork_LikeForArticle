# Generated by Django 3.1.6 on 2021-03-11 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20210311_1721'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='articletag',
            table='articel_tags_old',
        ),
    ]