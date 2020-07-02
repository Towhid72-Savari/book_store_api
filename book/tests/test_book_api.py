from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Book
from book.serializers import BookSerializer


BOOK_URL = reverse('book:book-list')


class PublicBooksApiTests(TestCase):
    """Test the Books API"""
    def setUp(self):
        self.client = APIClient()

    def test_retrieving_books(self):
        """Test that books list returned correctly"""
        Book.objects.create(title='Test Title', author='Test Author', publish_year=1990)
        Book.objects.create(title='example', author='example', publish_year=19)

        books = Book.objects.all().order_by('-title')
        res = self.client.get(BOOK_URL)
        serializer = BookSerializer(books, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_book_successful(self):
        """Test that creating a new bok is successful"""
        payload = {'title': 'Test', 'author': 'Test', 'publish_year': 1190}
        self.client.post(BOOK_URL, payload)

        exists = Book.objects.filter(
            title=payload['title'], author=payload['author']
        ).exists()
        self.assertTrue(exists)

    def test_create_book_invalid(self):
        """Test creating a new book with invalid payload"""
        payload = {'title': 'Test', 'author': '', 'publish_year': 1190}
        res = self.client.post(BOOK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)



