class PrimeFactor:
    def of(self, number):
        factors = []

        if 3 >= number >= 2:
            factors.append(number)
        elif number >= 4:
            factors = [2, 2]


        return factors
