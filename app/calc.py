import app
import math

class Calculator:
    def add(self, x, y):
        app.util.check_types(x, y)
        return x + y

    def substract(self, x, y):
        app.util.check_types(x, y)
        return x - y

    def multiply(self, x, y, user ='user1'):
        if not app.util.validate_permissions(f"{x} * {y}", user):
            raise TypeError('User has no permissions')
        app.util.check_types(x, y)
        return x * y

    def divide(self, x, y):
        app.util.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        app.util.check_types(x, y)
        return x ** y

    def sqrt(self, x):
        app.util.check_type(x)
        if x < 0:
            raise TypeError("Undefined square root for negative numbers")
        return math.sqrt(x) 

    def log10(self, x):
        app.util.check_type(x)
        if x <= 0:
            raise TypeError("Log Base 10 not set to negative numbers or zero")
        return math.log10(x) 


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
