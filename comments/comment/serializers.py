from rest_framework import serializers
from comments.comment.models import MainComment, SubComment


class MainCommentSerializer(serializers.ModelSerializer):
    sub_comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = MainComment
        fields = ('id', 'text', 'created', 'is_deleted', 'sub_comments')


class SubCommentSerializer(serializers.ModelSerializer):
    response_to_obj = serializers.ReadOnlyField()

    class Meta:
        model = SubComment
        fields = ('id', 'text', 'created', 'is_deleted', 'response_to', 'response_to_obj')
