from rest_framework.test import APITestCase
from rest_framework import status
from .models import FAQ

class FAQTests(APITestCase):
    def test_faq_translation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        faq.translate_faq()
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('question_hi', response.data[0])
        self.assertIn('answer_hi', response.data[0])
