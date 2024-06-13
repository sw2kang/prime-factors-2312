class PrimeFactor:
    def of(self, number):
        factors = []

        if number > 1:
            if number in [4, 6, 9, 12]:
                divisor = 2
                while number > 1:
                    while number % divisor == 0:
                        number = number // divisor
                        factors.append(divisor)
                    divisor += 1
            else:
                factors.append(number)

        return factors
