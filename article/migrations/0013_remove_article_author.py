# Generated by Django 3.1.6 on 2021-04-12 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20210315_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
