import unittest
from src.auth.signup import check_number, check_name


class SignupCaseTest(unittest.TestCase):
    def test_input_number(self):
        self.assertEqual(check_number("+79677513432"), True)
        self.assertEqual(check_number("79687513432"), False)
        self.assertEqual(check_number("898989898989"), False)
        self.assertEqual(check_number("89165433134"), True)

    def test_input_name(self):
        self.assertEqual(check_name("Ivan"), False)
        self.assertEqual(check_name("Иван"), True)
        self.assertEqual(check_name("/sdfdnkl"), False)
        self.assertEqual(check_name("иван"), False)
        self.assertEqual(check_name("/start"), False)


if __name__ == '__main__':
    unittest.main()
