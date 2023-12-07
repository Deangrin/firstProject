"""
calculator for first exercise
"""


def string_to_float(num):
    # receives a string and checks if it can be turned into float,
    # if not, inputs again and checks until can be, then returns it
    while True:
        try:
            return float(num)
        except ValueError:
            num = input("enter real number")


def calculate(num1, operator, num2):
    # receives two number and an operator from +, -, *, /, ^
    # and returns their calculation result
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return num1 ** num2


def main():
    # inputs two numbers and an operator, checking their validity,
    # and prints their calculation result
    num1 = input("enter first number")
    num1 = string_to_float(num1)
    operator = input("enter operator: +, -, *, /, ^")
    while operator not in ['+', '-', '*', '/', '^']:
        operator = input("enter one of the operators above")
    num2 = input("enter second number")
    num2 = string_to_float(num2)
    print(num1, operator, num2, "=", calculate(num1, operator, num2))


if __name__ == '__main__':
    main()
