class PrimeFactor:
    def of(self, number):
        factors = []

        if number > 1:
            if number == 4:
                while number % 2 == 0:
                    number = number // 2
                    factors.append(2)
            else:
                factors.append(number)

        return factors
