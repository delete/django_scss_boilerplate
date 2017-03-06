import io

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse
from django.test import TestCase

from backend.core.models import CreditCardNumber


class IndexViewTests(TestCase):

    def _get_temporary_text_file(self):
        text = io.StringIO()
        numbers = [
            '6\n',
            '4123456789123456\n',
            '5123-4567-8912-3456\n',
            '61234-567-8912-3456\n',
            '4123356789123456\n',
            '5133-3367-8912-3456\n',
            '5123 - 3567 - 8912 - 3456\n',
        ]
        for n in numbers:
            text.write(n)

        text_file = InMemoryUploadedFile(
            text,
            None,
            'foo.txt',
            'text',
            None,
            'utf-8'
        )
        text_file.seek(0)
        return text_file

    def setUp(self):
        self.data = {
            '_file': self._get_temporary_text_file()
        }
        self.results = {
            '4123456789123456': 'Valid',
            '5123-4567-8912-3456': 'Valid',
            '61234-567-8912-3456': 'Invalid',
            '4123356789123456': 'Valid',
            '5133-3367-8912-3456': 'Invalid',
            '5123 - 3567 - 8912 - 3456': 'Invalid',
        }
        self.url = reverse('core:index')

    def test_credit_card_creation(self):
        self.client.post(self.url, data=self.data)

        self.assertTrue(CreditCardNumber.objects.exists())

    def test_credit_card_status_code_200(self):
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(200, response.status_code)

    def test_credit_card_validation(self):
        self.client.post(self.url, data=self.data)

        for card in CreditCardNumber.objects.all():
            self.assertEqual(self.results[card.number], card.is_valid_number)

    def test_html(self):
        """Html must contain input tags"""

        response = self.client.post(self.url, data=self.data)
        tags = (
            ('<table', 1),
            ('<thead', 1),
            ('<tbody', 1),
            ('<tr', 7),
            ('type="submit"', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(response, text, count)
