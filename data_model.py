
# Note: Any function that I would want to implement is associated with corresponding data model functions or dunder methods
# Add -> __add__ , len -> __len__ etc.,
class Polynomial():
    def __init__(self, *coeffs) -> None:
        self.coeffs = coeffs

    def __repr__(self) -> str:
        return "Polynomial (*{!r})".format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x,y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)
    
    def __call__(self):
        pass

p1 = Polynomial(1, 2, 3) # x^2 + 2x + 3
p2 = Polynomial(3, 1, 2) # 3x^2 + x + 2

# Ide debugger
# >>> p1 = Polynomial(1, 2, 3)
# >>> p2 = Polynomial(3, 1, 2)
# >>> 
# >>> p1 
# Polynomial (*(1, 2, 3))
# >>> p2
# Polynomial (*(3, 1, 2))
# >>> p1 + p2
# Polynomial (*(4, 3, 5))
# >>> len(p1)
# 3
# >>> p1(p2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: __call__() takes 1 positional argument but 2 were given
# >>> p1()