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

    def test_prime_factor_4(self):
        self.assertEqual([2, 2], self.prime_factor.of(4))

    def test_prime_factor_6(self):
        self.assertEqual([2, 3], self.prime_factor.of(6))

    def test_prime_factor_9(self):
        self.assertEqual([3, 3], self.prime_factor.of(9))

    def test_prime_factor_12(self):
        self.assertEqual([2, 2, 3], self.prime_factor.of(12))
