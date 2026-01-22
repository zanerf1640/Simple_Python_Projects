"""
This is an advanced calculator program in Python that can perform various mathematical operations including 
numerics, algebra, calculus, statistical probability, and plotting functions.

Author: Zane Francis
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

#-----------------------------------------------------
# This class handles various numeric computations
#-----------------------------------------------------
class Numerics:

    def basic_operations(self, a, b, operation):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b
        else:
            raise ValueError("Unsupported operation")
        
    def remainder(self, a, b):
        return a % b
        
    def convert_to_fraction(self, decimal_number):
        return sp.Rational(decimal_number)
    
    def convert_to_decimal(self, fraction):
        return float(fraction)
    
    def least_common_multiple(self, a, b):
        return sp.lcm(a, b)
    
    def greatest_common_divisor(self, a, b):
        return sp.gcd(a, b)

#-----------------------------------------------------
# This class handles algebraic computations
#-----------------------------------------------------
class Algebra:

    def solve_quadratic(self, a, b, c):
        d = (b ** 2) - (4 * a * c)
        root1 = (-b + sp.sqrt(d)) / (2 * a)
        root2 = (-b - sp.sqrt(d)) / (2 * a)
        return root1, root2
    
    def factor_polynomial(self, expr):
        x = sp.symbols('x')
        transformations = standard_transformations + (
            implicit_multiplication_application,
            convert_xor,
        )
        polynomial = parse_expr(expr, transformations=transformations, local_dict={'x': x})
        polynomial = sp.nsimplify(polynomial)
        return sp.factor(polynomial)
    
    def expand_polynomial(self, expr):
        x = sp.symbols('x')
        transformations = standard_transformations + (
            implicit_multiplication_application,
            convert_xor,
        )
        polynomial = parse_expr(expr, transformations=transformations, local_dict={'x': x})
        return sp.expand(polynomial)
    
    def zero_of_function(self, func, var):
        variable = sp.symbols(var)
        transformations = standard_transformations + (
            implicit_multiplication_application,
            convert_xor,
        )
        f = parse_expr(func, transformations=transformations, local_dict={var: variable})
        return sp.solve(f, variable)
    
    def complete_square(self, a, b, c):
        h = -b / (2 * a)
        k = c - (b ** 2) / (4 * a)
        return a, h, k  # returns in the form a(x - h)^2 + k

#-----------------------------------------------------
# This class handles calculus operations
#-----------------------------------------------------
class Calculus:

    def derrivative(self, func, var):
        f = sp.sympify(func)
        variable = sp.symbols(var)
        return sp.diff(f, variable)
    
    def derrivative_at_point(self, func, var, point):
        f = sp.sympify(func)
        variable = sp.symbols(var)
        derivative = sp.diff(f, variable)
        return derivative.subs(variable, point)
    
    def integral(self, func, var):
        f = sp.sympify(func)
        variable = sp.symbols(var)
        return sp.integrate(f, variable)
    
    def integral_definite(self, func, var, a, b):
        f = sp.sympify(func)
        variable = sp.symbols(var)
        return sp.integrate(f, (variable, a, b))
    
    def limit(self, func, var, point):
        f = sp.sympify(func)
        variable = sp.symbols(var)
        return sp.limit(f, variable, point)
    
    def sum_of_series(self, series, var, n):
        s = sp.sympify(series)
        variable = sp.symbols(var)
        return sp.summation(s, (variable, 1, n))
    
    def taylor_series(self, func, var, point, n):
        f = sp.sympify(func)
        variable = sp.symbols(var)
        return sp.series(f, variable, point, n).removeO()

#-----------------------------------------------------
# This class handles probability calculations
#-----------------------------------------------------
class StatisticalProbability:

    def factorial(self, n):
        return sp.factorial(n)
    
    def permutations(self, n, r):
        # Number of permutations (nPr): n! / (n - r)!
        if r > n or n < 0 or r < 0:
            raise ValueError("Invalid values for permutations: require 0 <= r <= n")
        return sp.factorial(n) / sp.factorial(n - r)
    
    def combinations(self, n, r):
        return sp.binomial(n, r)
    
    def mean(self, data):
        return np.mean(data)
    
    def median(self, data):
        return np.median(data)
    
    def mode(self, data):
        values, counts = np.unique(data, return_counts=True)
        max_count_index = np.argmax(counts)
        return values[max_count_index]
    
    def standard_deviation(self, data):
        return np.std(data)
    
    def variance(self, data):
        return np.var(data)

#-----------------------------------------------------
# This class handles plotting functions
#-----------------------------------------------------
class Plotting:

    def plot_function(self, func, var, x_range):
        f = sp.sympify(func)
        variable = sp.symbols(var)
        x_vals = np.linspace(x_range[0], x_range[1], 400)
        f_lambdified = sp.lambdify(variable, f, modules=['numpy'])
        y_vals = f_lambdified(x_vals)

        plt.plot(x_vals, y_vals)
        plt.title(f'Plot of {func}')
        plt.xlabel(var)
        plt.ylabel('f({})'.format(var))
        plt.grid(True)
        plt.show()
    
    def plot_data(self, data_x, data_y, title='Data Plot', x_label='X-axis', y_label='Y-axis'):
        plt.scatter(data_x, data_y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)
        plt.show()
    
    def three__plot(self, func, var1, var2, x_range, y_range):
        f = sp.sympify(func)
        variable1 = sp.symbols(var1)
        variable2 = sp.symbols(var2)
        
        x_vals = np.linspace(x_range[0], x_range[1], 100)
        y_vals = np.linspace(y_range[0], y_range[1], 100)
        X, Y = np.meshgrid(x_vals, y_vals)
        f_lambdified = sp.lambdify((variable1, variable2), f, modules=['numpy'])
        Z = f_lambdified(X, Y)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_title(f'3D Plot of {func}')
        ax.set_xlabel(var1)
        ax.set_ylabel(var2)
        ax.set_zlabel('f({}, {})'.format(var1, var2))
        plt.show()

#-----------------------------------------------------
# Main program to interact with the user
#-----------------------------------------------------
while True:
    if __name__ == "__main__":
        print()
        print("---- Welcome to the Advanced Python Calculator ----")
        print("Choose an category:")
        print("1. Numerics")
        print("2. Algebra")
        print("3. Calculus")
        print("4. Statistical Probability")
        print("5. Plotting")
        print("6. Exit Program")
        
        choice = input("Enter choice (1-6):")

        # Choice 1 activates Numerics class
        if choice == '1':
            numerics = Numerics()
            print()
            print("Numerics operations can be performed here.")
            print("Choose an operation:")
            print("a. Basic Operations (add, subtract, multiply, divide):")
            print("b. Remainder")
            print("c. Convert to Fraction")
            print("d. Convert to Decimal")
            print("e. Least Common Multiple")
            print("f. Greatest Common Divisor")
            print("q. Go back to main menu")
            
            operation = input("Enter operation (a-f): ")
            # Add, Subtract, Multiply, Divide
            if operation == 'a':
                op = input("Enter operation (+, -, *, /): ")
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = numerics.basic_operations(a, b, op)
                print(f"---Result: {result}---")
            # Remainder
            elif operation == 'b':
                a = int(input("Enter dividend: "))
                b = int(input("Enter divisor: "))
                result = numerics.remainder(a, b)
                print(f"---Remainder: {result}---")
            # Convert to Fraction
            elif operation == 'c':
                decimal_number = float(input("Enter decimal number: "))
                result = numerics.convert_to_fraction(decimal_number)
                print(f"---Fraction: {result}---")
            # Convert to Decimal
            elif operation == 'd':
                fraction_input = input("Enter fraction (e.g., 3/4): ")
                fraction = sp.Rational(fraction_input)
                result = numerics.convert_to_decimal(fraction)
                print(f"---Decimal: {result}---")
            # Least Common Multiple
            elif operation == 'e':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result = numerics.least_common_multiple(a, b)
                print(f"---LCM: {result}---")
            # Greatest Common Divisor
            elif operation == 'f':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result = numerics.greatest_common_divisor(a, b)
                print(f"---GCD: {result}---")
            
            elif operation == 'q':
                continue
            # Invalid operation
            else:
                print("Invalid operation selected.")
        
        # Choice 2 activates Algebra class
        elif choice == '2':
            algebra = Algebra()
            print()
            print("Algebra operations can be performed here.")
            print("Choose an operation:")
            print("a. Solve Quadratic Equation")
            print("b. Factor Polynomial")
            print("c. Expand Polynomial")
            print("d. Find Zeros of Function")
            print("e. Complete the Square")
            print("q. Go back to main menu")
            
            operation = input("Enter operation (a-e): ")
            # Solve Quadratic Equation
            if operation == 'a':
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter coefficient c: "))
                roots = algebra.solve_quadratic(a, b, c)
                print(f"---Roots: {roots}---")
            # Factor Polynomial
            elif operation == 'b':
                expr = input("Enter polynomial expression (in terms of x): ")
                factored = algebra.factor_polynomial(expr)
                print(f"---Factored Polynomial: {factored}---")
            # Expand Polynomial
            elif operation == 'c':
                expr = input("Enter polynomial expression (in terms of x): ")
                expanded = algebra.expand_polynomial(expr)
                print(f"---Expanded Polynomial: {expanded}---")
            # Find Zeros of Function
            elif operation == 'd':
                func = input("Enter function (in terms of x): ")
                zeros = algebra.zero_of_function(func, 'x')
                print(f"---Zeros of the function: {zeros}---")
            # Complete the Square
            elif operation == 'e':
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter coefficient c: "))
                completed = algebra.complete_square(a, b, c)
                print(f"---Completed Square Form: {completed[0]}(x - {completed[1]})^2 + {completed[2]}---")
            
            elif operation == 'q':
                continue
            # Invalid operation
            else:
                print("Invalid operation selected.")

        # Choice 3 activates Calculus class
        elif choice == '3':
            calculus = Calculus()
            print()
            print("Calculus operations can be performed here.")
            print("Choose an operation:")
            print("a. Derivative")
            print("b. Derivative at a Point")
            print("c. Integral")
            print("d. Definite Integral")
            print("e. Limit")
            print("f. Sum of Series")
            print("g. Taylor Series")
            print("q. Go back to main menu")
            
            operation = input("Enter operation (a-g): ")
            # Derivative
            if operation == 'a':
                func = input("Enter function (in terms of x): ")
                derivative = calculus.derrivative(func, 'x')
                print(f"---Derivative: {derivative}---")
            # Derivative at a Point
            elif operation == 'b':
                func = input("Enter function (in terms of x): ")
                point = float(input("Enter point to evaluate derivative: "))
                derivative_at_point = calculus.derrivative_at_point(func, 'x', point)
                print(f"---Derivative at {point}: {derivative_at_point}---")
            # Integral
            elif operation == 'c':
                func = input("Enter function (in terms of x): ")
                integral = calculus.integral(func, 'x')
                print(f"---Indefinite Integral: {integral} + C---")
            # Definite Integral
            elif operation == 'd':
                func = input("Enter function (in terms of x): ")
                a = float(input("Enter lower limit a: "))
                b = float(input("Enter upper limit b: "))
                definite_integral = calculus.integral_definite(func, 'x', a, b)
                print(f"---Definite Integral from {a} to {b}: {definite_integral}---")
            # Limit
            elif operation == 'e':
                func = input("Enter function (in terms of x): ")
                point = float(input("Enter point to evaluate limit: "))
                limit_value = calculus.limit(func, 'x', point)
                print(f"---Limit as x approaches {point}: {limit_value}---")
            # Sum of Series
            elif operation == 'f':
                series = input("Enter series expression (in terms of n): ")
                n = int(input("Enter upper limit n: "))
                sum_series = calculus.sum_of_series(series, 'n', n)
                print(f"---Sum of Series up to n={n}: {sum_series}---")
            # Taylor Series
            elif operation == 'g':
                func = input("Enter function (in terms of x): ")
                point = float(input("Enter point to expand around:"))
                n = int(input("Enter number of terms n: "))
                taylor_series = calculus.taylor_series(func, 'x', point, n)
                print(f"---Taylor Series: {taylor_series}---")

            elif operation == 'q':
                continue
            # Invalid operation
            else:
                print("Invalid operation selected.")

        # Choice 4 activates StatisticalProbability class
        elif choice == '4':
            stats = StatisticalProbability()
            print()
            print("Statistical Probability operations can be performed here.")
            print("Choose an operation:")
            print("a. Factorial")
            print("b. Permutations")
            print("c. Combinations")
            print("d. Mean")
            print("e. Median")
            print("f. Mode")
            print("g. Standard Deviation")
            print("h. Variance")
            print("q. Go back to main menu")
            
            operation = input("Enter operation (a-h): ")
            # Factorial
            if operation == 'a':
                n = int(input("Enter number to compute factorial: "))
                result = stats.factorial(n)
                print(f"---Factorial: {result}---")
            # Permutations
            elif operation == 'b':
                n = int(input("Enter total items n: "))
                r = int(input("Enter items to choose r: "))
                result = stats.permutations(n, r)
                print(f"---Permutations: {result}---")
            # Combinations
            elif operation == 'c':
                n = int(input("Enter total items n: "))
                r = int(input("Enter items to choose r: "))
                result = stats.combinations(n, r)
                print(f"---Combinations: {result}---")
            # Mean
            elif operation == 'd':
                data = list(map(float, input("Enter data points separated by spaces: ").split()))
                result = stats.mean(data)
                print(f"---Mean: {result}---")
            # Median
            elif operation == 'e':
                data = list(map(float, input("Enter data points separated by spaces: ").split()))
                result = stats.median(data)
                print(f"---Median: {result}---")
            # Mode
            elif operation == 'f':
                data = list(map(float, input("Enter data points separated by spaces: ").split()))
                result = stats.mode(data)
                print(f"---Mode: {result}---")
            # Standard Deviation
            elif operation == 'g':
                data = list(map(float, input("Enter data points separated by spaces: ").split()))
                result = stats.standard_deviation(data)
                print(f"---Standard Deviation: {result}---")
            # Variance
            elif operation == 'h':
                data = list(map(float, input("Enter data points separated by spaces: ").split()))
                result = stats.variance(data)
                print(f"---Variance: {result}---")
            
            elif operation == 'q':
                continue
            # Invalid operation
            else:
                print("Invalid operation selected.")
        
        # Choice 5 activates Plotting class
        elif choice == '5':
            plotting = Plotting()
            print()
            print("Plotting operations can be performed here.")
            print("Choose an operation:")
            print("a. Plot Function")
            print("b. Plot Data")
            print("c. 3D Plot")
            
            operation = input("Enter operation (a-c): ")
            # Plot Function
            if operation == 'a':
                func = input("Enter function to plot (in terms of x): ")
                x_start = float(input("Enter x-axis start value: "))
                x_end = float(input("Enter x-axis end value: "))
                plotting.plot_function(func, 'x', (x_start, x_end))
            # Plot Data
            elif operation == 'b':
                data_x = list(map(float, input("Enter x data points separated by spaces: ").split()))
                data_y = list(map(float, input("Enter y data points separated by spaces: ").split()))
                title = input("Enter plot title: ")
                x_label = input("Enter x-axis label: ")
                y_label = input("Enter y-axis label: ")
                plotting.plot_data(data_x, data_y, title, x_label, y_label)
            # 3D Plot
            elif operation == 'c':
                func = input("Enter function to plot (in terms of x and y): ")
                x_start = float(input("Enter x-axis start value: "))
                x_end = float(input("Enter x-axis end value: "))
                y_start = float(input("Enter y-axis start value: "))
                y_end = float(input("Enter y-axis end value: "))
                plotting.three__plot(func, 'x', 'y', (x_start, x_end), (y_start, y_end))
            
            elif operation == 'q':
                continue
            # Invalid operation
            else:
                print("Invalid operation selected.")
        
        # Exit Program
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        # Invalid choice
        else:
            print("Invalid choice selected.")