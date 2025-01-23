from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from users.models import User
from .models import News

class NewsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_news(self):
        data = {
            'title': 'Test News',
            'content': 'Test Content'
        }
        response = self.client.post(reverse('news-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(News.objects.get().title, 'Test News')