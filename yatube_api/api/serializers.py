from rest_framework import serializers
from posts.models import Post, Group, Comment

class PostSerializer(serializers.ModelSerializer):
    # Указываем, что автором будет username, и поле доступно только для чтения
    author = serializers.SlugRelatedField(
        slug_field='username', 
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', 
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        # ID поста мы берем из URL, поэтому запрещаем передавать его в теле запроса
        read_only_fields = ('post',)