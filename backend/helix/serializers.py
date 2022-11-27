from rest_framework import serializers
from .models import Question
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'question')
        
    
    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

class QuestionSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    # JUST ID
    #comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'text', 'completed', "comments")


