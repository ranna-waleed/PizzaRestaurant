import unittest
from src.payment import PayPalPayment, CreditCardPayment

class TestPayment(unittest.TestCase):
    def test_paypal_payment(self):
        payment = PayPalPayment()
        self.assertIsNone(payment.pay(10.0))

    def test_credit_card_payment(self):
        payment = CreditCardPayment()
        self.assertIsNone(payment.pay(10.0))

if __name__ == '__main__':
    unittest.main()