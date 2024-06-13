from unittest import TestCase

from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_prime_factor_1(self):
        prime_factor = PrimeFactor()
        self.assertEqual([], prime_factor.of(1))
