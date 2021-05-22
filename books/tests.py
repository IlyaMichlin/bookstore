from django.test import TestCase
from django.urls import reverse
from .models import Book


# Create your tests here.
class BookTests(TestCase):
    test_title = 'Test Title'
    test_author = 'Test Author'
    test_price = '25.00'

    def setUp(self):
        self.book = Book.objects.create(
            title=self.test_title,
            author=self.test_author,
            price=self.test_price,
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', self.test_title)
        self.assertEqual(f'{self.book.author}', self.test_author)
        self.assertEqual(f'{self.book.price}', self.test_price)

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.test_title)
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/book/418564856/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.test_title)
        self.assertTemplateUsed(response, 'books/book_detail.html')
