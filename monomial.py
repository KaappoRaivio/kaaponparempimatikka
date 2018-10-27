class Monomial:
    def __init__(self, coeff: int or float, var: chr):
        self.coeff = coeff
        self.chr = var

    def __str__(self):
        return f"{self.coeff}{self.chr}"