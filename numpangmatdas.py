from sympy import symbols, limit

x = symbols('x')
expr = (x**2 - 4) / (x - 2)
result = limit(expr, x, 2)
print(result)  # Output: 4
