from rest_framework import serializers

from posts.models import Comment, Group, Follow, Post, User


ALL_FIELDS = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Represents serializer for Comment model."""
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ALL_FIELDS


class PostSerializer(serializers.ModelSerializer):
    """Represents serializer for Post model."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = ALL_FIELDS


class GroupSerializer(serializers.ModelSerializer):
    """Represents serializer for Group model."""
    class Meta:
        model = Group
        fields = ALL_FIELDS


class FollowSerializer(serializers.ModelSerializer):
    """Represents serializer for Follow model."""
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            ),
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'user')
            )
        ]
