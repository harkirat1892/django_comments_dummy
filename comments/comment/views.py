# from django.shortcuts import render
from comments.comment.models import MainComment, SubComment
from rest_framework import viewsets
from comments.comment.serializers import MainCommentSerializer, SubCommentSerializer


class MainCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MainComment.objects.all().order_by('-created')
    serializer_class = MainCommentSerializer


class SubCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sub comments to be viewed or edited.
    """
    queryset = SubComment.objects.all().order_by('-created')
    serializer_class = SubCommentSerializer
