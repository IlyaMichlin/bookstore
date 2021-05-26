from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse
from .models import Book, Review


# Create your tests here.
class BookTests(TestCase):
    test_title = 'Test Title'
    test_author = 'Test Author'
    test_price = '25.00'

    test_username = 'testuser'
    test_email = 'testuser@mail.com'
    test_password = 'testpass123'

    test_review = 'Test review text.'

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username=self.test_username,
            email=self.test_email,
            password=self.test_password,
        )

        self.special_permission = Permission.objects.get(codename='special_status')

        self.book = Book.objects.create(
            title=self.test_title,
            author=self.test_author,
            price=self.test_price,
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review=self.test_review,
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', self.test_title)
        self.assertEqual(f'{self.book.author}', self.test_author)
        self.assertEqual(f'{self.book.price}', self.test_price)

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email=self.test_email, password=self.test_password)
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.test_title)
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/books/' % (reverse('account_login')))
        response = self.client.get('%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

    def test_book_detail_view_with_permissions(self):
        self.client.login(email=self.test_email, password=self.test_password)
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/book/418564856/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.test_title)
        self.assertContains(response, self.test_review)
        self.assertTemplateUsed(response, 'books/book_detail.html')
