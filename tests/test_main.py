import unittest
from main import check_age, check_email, longest_film


class TestCheckAge(unittest.TestCase):
    def test_age_check(self):
        ages = [18, 19, 17]
        expected_results = ['Доступ разрешён', 'Доступ разрешён', 'Доступ запрещён']
        for age, expected_result in zip(ages, expected_results):
            actual_result = check_age(age)
            self.assertEqual(actual_result, expected_result)


class TestCheckEmail(unittest.TestCase):
    def test_check_email(self):
        valid_emails = ["test@example.com", "test.test@example.com", "test_test@example.com"]
        invalid_emails = ["test.example.com", "test@example", "test example.com", ""]

        for email in valid_emails:
            self.assertTrue(check_email(email))

        for email in invalid_emails:
            self.assertFalse(check_email(email))


class TestCheckFilm(unittest.TestCase):
    def test_max_len_film(self):
        list_films = ['Аладин', 'Мадагаскар', 'Бетховен']
        max_len_film = max(list_films, key=len)
        self.assertEqual(longest_film(list_films), max_len_film)
