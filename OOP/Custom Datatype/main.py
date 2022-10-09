# Create custom datatype
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"
    
    # Fraction add
    def __add__(self, other):
        # 4/5 + 5/6
        # 4/5 + 5/5
        temp_num = self.numerator * other.denominator + other.numerator * self.denominator  # when both the denominators are unique
        temp_den = self.denominator * other.denominator
        return f"{temp_num}/{temp_den}"
    
    # Fraction sub
    def __sub__(self, other):
        temp_num = self.numerator * other.denominator - other.numerator * self.denominator
        temp_den = self.denominator * other.denominator
        return f"{temp_num}/{temp_den}"

    # Fraction mul
    def __mul__(self, other):
        temp_num = self.numerator * other.numerator
        temp_den = self.denominator * other.denominator
        return f"{temp_num}/{temp_den}"
    
    # Fraction div
    def __truediv__(self, other):
        temp_num = self.numerator * other.denominator
        temp_den = self.denominator * other.numerator
        return f"{temp_num}/{temp_den}"



frac1 = Fraction(4,5)
frac2 = Fraction(5,6)
# frac1 = Fraction(4,5)
# frac2 = Fraction(5,5)
print(frac1)
print(frac2)
print(frac1 / frac2)
