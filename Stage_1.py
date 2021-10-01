# Work on project. Stage 1/4: Mini-calculator

# Description
# People learn new things in one way or another. Learning
# sometimes means that you need to check your comprehension
# by taking a test. It also requires a person (or a program) to
# check your answers. You may have been in a situation when you
# think that you have solved the task correctly, but your professor
# has a different (sometimes wrong!) answer, It happens;
# everybody makes mistakes.

# Not our application though. It should calculate the solution in a
# very precise manner. We need to make a simple calculator that
# can evaluate expressions like a + b, a - b, a * b. We will
# leave the division aside for now.

# Objectives
# 1. A user inputs a line that looks like a simple mathematical
#    operation.
# 2. The application should print the result of the operation.

# Examples
# The greater-than symbol followed by a space ( > ) represents
# the user input. Note that it's not part of the input.

# Example 1:
# > 5 + 7
# 12

# Example 2:
# > 3 * 100
# 300

# Example 3:
# > 5 - 10

# Example 4:
# > 8 * 0
# 0

class Minicalculator:
    def __init__(self):
        self.number_1 = None
        self.operator = None
        self.number_2 = None

    def process(self):
        self.number_1, self.operator, self.number_2 = input().split()
        arithmetic = {'*': lambda x, y: x * y,
                      '+': lambda x, y: x + y,
                      '-': lambda x, y: x - y}
        return arithmetic[self.operator](int(self.number_1), int(self.number_2))
        # return eval(input())

def main():
    calculator = Minicalculator()
    print(calculator.process())


if __name__ == '__main__':
    main()
