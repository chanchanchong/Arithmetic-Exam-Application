# Work on project. Stage 2/4: Task generator

# Description
# Any test includes at least one task. This task can vary in
# difficulty and required timeframes. There can be more than one
# task; they can demand different forms of answers. One thing
# remains - if there's a task, there's a solution. And we need to
# assess it.

# Math tasks can vary in difficulty. 1 * 3 is easy. 75 * 34 is a bit
# more difficult. For the next stage, think about levels of
# difficulty that you can add!


# For now, let's use random number from 2 to 9 and integer
# operations: +, - and *.

# Objectives
# 1. Generate a math task that looks like a math operation. Use
#    the requirements above. Print it.
# 2. Read the answer from a user.
# 3. Check whether the answer is correct. Print Right! or
#    Wrong!

# Examples
# The greater-than symbol followed by a space (> ) represents
# the user input. Note that it's not part of the input.

# Example 1:
# 5 * 7
# > 35
# Right!

# Example 2:
# 5 * 7
# > 5
# Wrong!

# write your code here
import random


class ArithmeticExamApplication:
    def __init__(self):
        self.operators = ['+', '-', '*']
        self.numbers = [_ for _ in range(2, 10)]
        self.operator = random.choice(self.operators)
        self.num_1 = random.choice(self.numbers)
        self.num_2 = random.choice(self.numbers)
        self.answer = None
        self.right_message = "Right!"
        self.wrong_message = "Wrong!"
        self.right_answer = None
        self.question = self.operation_generator()

    def checker(self):
        self.right_answer = eval(self.question)
        print(self.question)
        self.answer = int(input())
        print(self.right_message if self.right_answer == self.answer else self.wrong_message)

    def operation_generator(self):
        self.operator = random.choice(self.operators)
        self.num_1 = random.choice(self.numbers)
        self.num_2 = random.choice(self.numbers)
        return f'{self.num_1} {self.operator} {self.num_2}'

    def start(self):
        self.checker()


def main():
    exam = ArithmeticExamApplication()
    exam.start()


if __name__ == '__main__':
    main()
