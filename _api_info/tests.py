from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch


class IpInfoTests(APITestCase):
    @patch('requests.get')
    def test_get_my_ip_info(self, mock_get):
        # Настройка mock-объекта
        mock_response = {
            "ip": "8.8.8.8",
            "country": "US",
            "city": "Mountain View",
            "org": "Google LLC",
            "timezone": "America/Los_Angeles",
            "loc": "37.3860,-122.0838",
            "link": "https://www.google.com/maps?q=37.3860,-122.0838"
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        url = reverse('IpInfo')
        response = self.client.get(url, HTTP_X_FORWARDED_FOR='8.8.8.8')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['ip'], '8.8.8.8')
        self.assertEqual(response.data['data']['country'], 'US')
        self.assertEqual(response.data['data']['city'], 'Mountain View')
        self.assertEqual(response.data['data']['org'], 'Google LLC')
        self.assertEqual(response.data['data']['timezone'], 'America/Los_Angeles')
        self.assertEqual(response.data['data']['link'], 'https://www.google.com/maps?q=37.3860,-122.0838')

    @patch('requests.get')
    def test_post_ip_info(self, mock_get):
        # Настройка mock-объекта
        mock_response = {
            "ip": "8.8.8.8",
            "country": "US",
            "city": "Mountain View",
            "org": "Google LLC",
            "timezone": "America/Los_Angeles",
            "loc": "37.3860,-122.0838",
            "link": "https://www.google.com/maps?q=37.3860,-122.0838"
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        url = reverse('IpInfo')
        response = self.client.post(url, {'ip': '8.8.8.8'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['ip'], '8.8.8.8')
        self.assertEqual(response.data['data']['country'], 'US')
        self.assertEqual(response.data['data']['city'], 'Mountain View')
        self.assertEqual(response.data['data']['org'], 'Google LLC')
        self.assertEqual(response.data['data']['timezone'], 'America/Los_Angeles')
        self.assertEqual(response.data['data']['link'], 'https://www.google.com/maps?q=37.3860,-122.0838')

    @patch('requests.get')
    def test_get_my_ip_info_no_ip(self, mock_get):
        # Настройка mock-объекта для случая отсутствия loc
        mock_response = {
            "ip": "8.8.8.8",
            "country": "US",
            "city": "Mountain View",
            "org": "Google LLC",
            "timezone": "America/Los_Angeles",
            "loc": None  # Здесь loc отсутствует
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        url = reverse('IpInfo')
        response = self.client.get(url, HTTP_X_FORWARDED_FOR='8.8.8.8')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['ip'], '8.8.8.8')
        self.assertEqual(response.data['data']['country'], 'US')
        self.assertEqual(response.data['data']['city'], 'Mountain View')
        self.assertEqual(response.data['data']['org'], 'Google LLC')
        self.assertEqual(response.data['data']['timezone'], 'America/Los_Angeles')
        self.assertIsNone(response.data['data'].get('link'))
