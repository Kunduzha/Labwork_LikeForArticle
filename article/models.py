from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='Заголовок',
        validators=(MinLengthValidator(5),)
    )
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Контент')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles'
    )
    tags = models.ManyToManyField(
        'article.Tag',
        related_name='articles',
        db_table='article_tags'
    )

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        permissions = [
            ('сan_have_piece_of_pizza', 'Может съесть кусочек пиццы')
        ]

    def __str__(self):
        return f'{self.id}. {self.author}: {self.title}'


class Comment(BaseModel):
    article = models.ForeignKey(
        'article.Article',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Статья',
        null=False,
        blank=False
    )
    comment = models.CharField(max_length=200, verbose_name='Комментарий', null=False, blank=False)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='comments'
    )

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    
    def __str__(self):
        return f'{self.author}: {self.comment}'




class LikeArticle(models.Model):
    article = models.ForeignKey(
        'article.Article',
        on_delete=models.CASCADE,
        related_name='like_article',
        verbose_name='Статья',
        null=False,
        blank=False)

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_like_article'
    )

    class Meta:
        db_table = 'like_article'
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'

    def __str__(self):
        return f'{self.article}: {self.user}'

class LikeComment(models.Model):
        comment = models.ForeignKey(
            'article.Comment',
            on_delete=models.CASCADE,
            related_name='like_comment',
            verbose_name='комментарий',
            null=False,
            blank=False)

        user = models.ForeignKey(
            get_user_model(),
            on_delete=models.SET_NULL,
            null=True,
            related_name='user_like_comment'
        )

        class Meta:
            db_table = 'like_comment'
            verbose_name = 'лайк'
            verbose_name_plural = 'лайки'

        def __str__(self):
            return f'{self.comment}: {self.user}'
    #
    # def like(self, article):
    #     if not self.is_liking(article):
    #         self.liked.append(article)
    #
    # def unlike(self, article):
    #     if self.is_liking(article):
    #         self.liked.remove(article)
    #
    # def is_liking(self, post):
    #     return self.liked.filter(
    #         get_user_model().c.liked_id == post.id).count() > 0


class Tag(BaseModel):
    tag = models.CharField(max_length=200, verbose_name='Тэг')

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    
    def __str__(self):
        return self.tag
