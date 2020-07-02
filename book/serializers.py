from rest_framework import serializers
from core.models import Book


class BookSerializer(serializers.ModelSerializer):
    """Serializes the book objects"""

    class Meta:
        model = Book
        fields = ('title', 'author', 'publish_year')
