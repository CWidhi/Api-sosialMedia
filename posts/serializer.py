from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    img = serializers.FileField(required=False)
    caption = serializers.CharField(required=False)
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'caption', 'img', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
        
    def validate(self, attrs):
        if self.instance is None:
            missing_fields = []
            if not attrs.get('caption'):
                missing_fields.append('caption')
            if not attrs.get('img'):
                missing_fields.append('img')
            if missing_fields:
                raise serializers.ValidationError({
                    field: f"This field is required for creation." for field in missing_fields
                })
        return attrs