from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'news', 'user', 'content', 'created_at', 'parent', 'replies']

    def get_replies(self, obj):
        if obj.parent is None:
            return CommentSerializer(obj.comment_set.all(), many=True).data
        return []