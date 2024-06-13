from unittest import TestCase

from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def setUp(self):
        super().setUp()
        self.prime_factor = PrimeFactor()

    def test_prime_factor_1(self):
        self.assertEqual([], self.prime_factor.of(1))

    def test_prime_factor_2(self):
        self.assertEqual([2], self.prime_factor.of(2))

    def test_prime_factor_3(self):
        self.assertEqual([3], self.prime_factor.of(3))
