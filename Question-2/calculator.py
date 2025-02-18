# You are building a calculator app. Write a Python function calculate() that takes two
# numbers and an operator (+, -, *, /) as input and returns the result.

def calculate(num1: int, num2: int, operator: str):
    if operator == '+':
        return (num1 + num2)
    elif operator == '-':
        return (num1 - num2)
    elif operator == '*':
        return (num1 * num2)
    elif operator == '/':
        return (num1 / num2)