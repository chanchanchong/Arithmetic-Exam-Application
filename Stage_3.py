# Stage 3/4: More tasks needed_

# Description
# Let's write an application that assesses the user's knowledge.
# Many people get nervous during exams; they can accidentally
# hit wrong key, confuse , with . in floats, and so on. Our
# application should allow some room for errors and give a
# person the opportunity to correct the typo.

# Objectives
# 1. The application should give the user 5 tasks. The tasks
#    are akin to the previous stage: two numbers from 2 to
#    9 and an integer operation.

# 2. The user receives one task, prints the answer. If the
#    answer contains a typo (letters or otherwise empty), the
#    program should print Incorrect format. and ask
#    to re-enter the answer. Repeat until the answer is in the
#    correct format. If the answer is a number, print
#    Right! or Wrong! depending on the answer and
#    carry on to the next question.

# 3. After five tasks, output Your mark is n/5. where
#    n is the number of correct answers.

# Example
# The greater-than symbol followed by a space ( > ) represents
# the user input. Note that it's not part of the input.

# Example 1: An example of the output
# 3 + 8
# > 11q
# Incorrect format.
# > eleven
# Incorrect format.
# > 11
# Right!
# 5 * 3
# > 35
# Right!
# 2 - 5
# > -4
# Wrong!
# 3 * 3
# 9
# Right!
# 8 + 3
# > 11
# Right!
# Your mark is 4/5.

import random


class ArithmeticExamApplication:
    def __init__(self):
        self.operators = ['+', '-', '*']
        self.numbers = [_ for _ in range(2, 10)]
        self.operator = None
        self.num_1 = None
        self.num_2 = None
        self.answer = None
        self.right_message = "Right!"
        self.wrong_message = "Wrong!"
        self.incorrect_message = "Incorrect format."
        self.question = None
        self.right_answer = None
        self.correct_answer = 0
        self.mark_message = ''

    def checker(self):
        self.question = self.operation_generator()
        self.right_answer = eval(self.question)
        print(self.question)
        while True:
            # print(self.right_message if self.right_answer == self.answer else self.wrong_message)
            try:
                self.answer = int(input())
                if self.right_answer == self.answer:
                    print(self.right_message)
                    self.correct_answer += 1
                    break
                else:
                    print(self.wrong_message)
                    break
            except ValueError:
                print(self.incorrect_message)

    def operation_generator(self):
        self.operator = random.choice(self.operators)
        self.num_1 = random.choice(self.numbers)
        self.num_2 = random.choice(self.numbers)
        return f'{self.num_1} {self.operator} {self.num_2}'

    def start(self):
        self.exam_loop()

    def exam_loop(self):
        for _ in range(5):
            self.checker()
        self.mark_message = self.mark()
        print(self.mark_message)

    def mark(self):
        return f'Your mark is {self.correct_answer}/5.'


def main():
    exam = ArithmeticExamApplication()
    exam.start()


if __name__ == '__main__':
    main()
