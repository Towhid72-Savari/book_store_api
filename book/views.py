from rest_framework import mixins, viewsets
from core.models import Book
from book import serializers


class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage tags in database"""
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    def perform_create(self, serializer):
        """Create a new book"""
        serializer.save()
