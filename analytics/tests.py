from django.test import TestCase, Client
from django.urls import reverse


class AnalyticsAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_key_stats_endpoint(self):
        url = "/api/analytics/key-stats/"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        # Check keys and demo values
        self.assertIn("total_students", data)
        self.assertEqual(data.get("total_students"), 1245)
        self.assertIn("male_students", data)
        self.assertIn("female_students", data)
