import unittest
import requests


class TestYandexDisc(unittest.TestCase):
    def setUp(self):
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Authorization': 'OAuth your_token'}
        self.param = {'path': 'image'}

    def test_create_folder(self):
        test_data = [
            ('put', 201, self.url, self.headers, self.param),
            ('get', 200, self.url, self.headers, self.param),
            ('post', 405, self.url, self.headers, self.param),
            ('put', 400, self.url, self.headers, {}),
        ]

        for i, (method, expected_status_code, url, headers, param) in enumerate(test_data):
            with self.subTest(method=method, status_code=expected_status_code):
                response = requests.request(method, url, headers=headers, params=param)
                self.assertEqual(response.status_code, expected_status_code)
