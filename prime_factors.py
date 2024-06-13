class PrimeFactor:
    def of(self, number):
        factors = []

        if number > 1:
            divisor = 2
            while number > 1:
                while number % divisor == 0:
                    number = number // divisor
                    factors.append(divisor)
                divisor += 1

        return factors
