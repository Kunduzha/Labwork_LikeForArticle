# Generated by Django 3.1.6 on 2021-05-18 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0016_auto_20210412_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_comment', to='article.comment', verbose_name='комментарий')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_like_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'лайк',
                'verbose_name_plural': 'лайки',
                'db_table': 'like_comment',
            },
        ),
        migrations.CreateModel(
            name='LikeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_article', to='article.article', verbose_name='Статья')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_like_article', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'лайк',
                'verbose_name_plural': 'лайки',
                'db_table': 'like_article',
            },
        ),
    ]
