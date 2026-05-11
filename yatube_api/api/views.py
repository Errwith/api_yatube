from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    # Группы по заданию можно только получать (GET), 
    # поэтому используем ReadOnlyModelViewSet
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        # Получаем id поста из URL
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        # Возвращаем все комментарии конкретного поста
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        # При сохранении привязываем комментарий к автору и посту
        serializer.save(author=self.request.user, post=post)