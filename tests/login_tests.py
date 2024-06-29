import unittest
from src.srm.srm_bot import check_crm
from src.auth.login import checking_number, check_name


class SignupCaseTest(unittest.TestCase):
    async def test_input_number(self):
        self.assertEqual(await checking_number("+79677513432"), True)
        self.assertEqual(await checking_number("79687513432"), False)
        self.assertEqual(await checking_number("898989898989"), False)
        self.assertEqual(await checking_number("89165433134"), True)
        self.assertEqual(await checking_number("+79213224013"), True)

    async def test_input_name(self):
        self.assertEqual(await check_name("Ivan"), False)
        self.assertEqual(await check_name("Иван"), True)
        self.assertEqual(await check_name("/sdfdnkl"), False)
        self.assertEqual(await check_name("иван"), False)
        self.assertEqual(await check_name("/start"), False)

    async def test_input_crm(self):
        self.assertEqual(await check_crm("+79677513432"), False)
        self.assertEqual(await check_crm("+79213224013"), True)


if __name__ == '__main__':
    unittest.main()
