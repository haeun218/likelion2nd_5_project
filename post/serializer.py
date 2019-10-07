from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'title', 'body']
        read_only_fields = ('title',) #'', 쉼표 꼭! 쉼표 없으면 문자열로 인식