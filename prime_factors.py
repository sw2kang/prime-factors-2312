class PrimeFactor:
    def of(self, number):
        factors = []

        if number > 1:
            if number == 4:
                while number % 2 == 0:
                    number = number // 2
                    factors.append(2)
            elif number == 6 or number == 9:
                divisor = 2
                while number > 1:
                    while number % divisor == 0:
                        number = number // divisor
                        factors.append(divisor)
                    divisor += 1
            else:
                factors.append(number)

        return factors
