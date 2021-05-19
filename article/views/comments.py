from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.views import View
from django.views.generic import CreateView
from django.shortcuts import reverse, get_object_or_404, redirect

from article.forms import CommentForm
from article.models import Comment, Article, LikeComment


class ArticleCommentCreate(PermissionRequiredMixin, CreateView):
    template_name = 'comments/create.html'
    form_class = CommentForm
    model = Comment
    permission_required = 'article.add_comment'

    def get_success_url(self):
        return reverse(
            'article:view',
            kwargs={'pk': self.kwargs.get('pk')}
        )
    
    def form_valid(self, form):
        article = get_object_or_404(Article, id=self.kwargs.get('pk'))

        comment = form.instance
        comment.article = article
        comment.author = self.request.user

        return super().form_valid(form)


class LikeForComment(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            LikeComment.objects.get(comment=comment, user=user)
            return HttpResponseForbidden("error")
        except LikeComment.DoesNotExist:
            LikeComment.objects.create(comment=comment, user=user)
        return HttpResponse(comment.like_comment.count())


class UnlikeForComment(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            like_comment = LikeComment.objects.get(comment=comment, user=user)
            like_comment.delete()
            return HttpResponse(comment.like_comment.count())
        except LikeComment.DoesNotExist:
            return HttpResponseForbidden("error")