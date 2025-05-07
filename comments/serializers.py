from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id',  'post', 'author', 'created_at', 'updated_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        return value