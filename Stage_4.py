# Stage 4/4: Adding marks

# Description

# Simple tasks are good for younger kinds, but math can be more
# difficult and more interesting! Quadratic equations,
# trigonometry, and a lot of other interesting things. Math library
# can help you with that.

# Sometimes students want to save the results of the test. This is
# useful for viewing the learning dynamics on a topic or to
# identify difficult tasks.

# At this stage, let's add integral squares. Of course, you can add
# more difficulty levels later.

# Objectives

# 1. With the first message, the program should ask for a
#    difficulty level:
#    1 - simple operations with numbers 2 - 9
#    2 - integral squares 11 - 29
# 2. A user enters an answer.
#    For the first difficulty level: the task is a simple math
#    operation; the answer is the result of the operation.
#    For the second difficulty level: the task is an integer; the
#    answer is the square of this number.
#    In case of another input: ask to re-enter. Repeat until
#    the format is correct.
# 3. The application gives 5 tasks to a user.
# 4. The user receives one task, prints the answer.
#    If the answer contains a typo. print Incorrect
#    format. and ask to re-enter the answer. Repeat until
#    the answer is in the correct format.
#    If the answer is a number, print Right! or Wrong!
#    Go the next question.
# 5. After five answers, print Your mark is N/5. where
#    N is the number of correct answers.
# 6. Output Would you like to save you result
#    to the file? Enter yes or no.
#    In case of yes, YES, y, Yes: the app should ask
#    the username and write Name: n/5 in level X
#    (<level description>). (X stands for the level
#    number) in the results.txt file. For example-
#    Alex: 3/5 in level 1 (simple operations
#    with numbers 2-9).
#    The results should be saved to the file immediately
#    after the user gave the positive answer to the question
#    Would you like to save your result to the file?
#    If the results.txt does not exist, you should
#    create it.
# 7. In case of no or any other word: exit the program.

# Example

# The greater-than symbol followed by a space ( > ) represents
# the user input. Note that it's not part of the input.

# Example 1:
# Which level do you want? Enter a number:
# 1 - simple operations with numbers 2-9
# 2 - integral squares of 11-29
# > 11
# Incorrect format.
# Which level do you want? Enter a number:
# 1 - simple operations with numbers 2-9
# 2 - integral squares of 11-29
# > 2
# 11
# > 121
# Right!
# 15
# 100
# Wrong!
# 21
# 441'
# Wrong format! Try again.
# 21
# > 441
# Right!
# 17
# > 289
# Right!
# 13
# > 169
# Right!
# Your mark is 4/5. Would you like to save the
# result? Enter yes or no.
# > yes
# What is your name?
# > Kate
# The results are saved in "results".txt".

# Afterword
# After finishing this stage, you are totally free to improve the
# project in any way you like to make it a more convenient and
# useful tool.

# You can add any features to your application. It will not be
# verified by tests, so there are no strict requirements.

# Sample ideas:
# 1. Add a complex exam. Increase a difficulty level on the
#    fly. For example, if a person passed the 1st level, start
#    the 2nd one immediately.
# 2. You can add a correction level: store the tasks with
#    wrong answers and give them next time.
# 3. Add more difficulty levels.
# 4. Track the time (read about Timer).
# 5. Write a more detailed report to a file with the results.
# 6. Show previous results inside the app (show lines from
#    results.txt that contains the username)
# 7. Any other improvement that might be useful!
import random
import sys


class ArithmeticExamApplication:

    def __init__(self):
        # for expression generator
        self.operators = ['+', '-', '*']
        self.yes = ['yes', 'Yes', 'YES', 'y']
        self.numbers = None
        self.operator = None
        self.num_1 = None
        self.num_2 = None

        # messages
        self.right_message = "Right!"
        self.wrong_message = "Wrong!"
        self.incorrect_message = "Incorrect format."
        self.mark_message = None
        self.introductory_message = """Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29"""
        self.one_message = "simple operations with numbers 2-9"
        self.two_message = "integral squares of 11-29"
        self.saving_message = "Would you like to save the result? Enter yes or no."
        # for checker
        self.question = None
        self.right_answer = None

        self.answer = None
        self.right_answer = None
        self.level_description = 0
        # for score
        self.score = 0

        # for start
        self.level = None

    def level_one(self):
        self.question = self.expression_generator()  # picking the expression
        self.right_answer = eval(self.question)  # solving the expression
        print(self.question)
        while True:
            try:
                self.answer = int(input())
                if self.right_answer == self.answer:  # correct answer
                    print(self.right_message)
                    # add 1 to score
                    self.score += 1
                    break
                else:
                    print(self.wrong_message)
                    break
            except ValueError:
                print(self.incorrect_message)

    # returning a randomized expression
    def expression_generator(self):
        self.numbers = [_ for _ in range(2, 10)]
        self.operator = random.choice(self.operators)  # random operator
        self.num_1 = random.choice(self.numbers)  # random single digit
        self.num_2 = random.choice(self.numbers)  # random single digit
        return f'{self.num_1} {self.operator} {self.num_2}'

    def integral_squares(self):
        self.numbers = [_ for _ in range(11, 30)]
        self.num_1 = random.choice(self.numbers)
        return f'{self.num_1}'

    def level_two(self):
        self.question = self.integral_squares()
        self.right_answer = eval(self.question + ' ** 2')
        print(self.question)
        while True:
            try:
                self.answer = int(input())
                if self.right_answer == self.answer:  # correct answer
                    print(self.right_message)
                    # add 1 to score
                    self.score += 1
                    break
                else:
                    print(self.wrong_message)
                    break
            except ValueError:
                print(self.incorrect_message)

    def start(self):
        while True:
            try:
                print(self.introductory_message)
                self.level = input()
                if len(self.level) == 1:
                    if int(self.level) == 1:
                        self.level_description = 1
                        self.exam_loop_one()
                        break
                    elif int(self.level) == 2:
                        self.level_description = 2
                        self.exam_loop_two()
                        break
                    else:
                        print(self.wrong_message)
                        continue
                else:
                    print(self.incorrect_message)
                    continue
            except ValueError:
                print(self.incorrect_message)

    def exam_loop_one(self):
        [self.level_one() for _ in range(5)]
        self.save()

    def exam_loop_two(self):
        [self.level_two() for _ in range(5)]
        self.save()

    def mark(self):
        return f'Your mark is {self.score}/5.' + self.saving_message

    def save(self):
        self.mark_message = self.mark()
        print(self.mark_message)
        self.answer = input()
        if self.answer in self.yes:
            print("What is your name?")
            username = input()
            with open('results.txt', 'a') as results:
                results.write(f'{username}: {self.score}/5 in level {self.level_description} ({ self.one_message if self.level_description == 1 else self.two_message}).')
            print('The results are saved in "results.txt".')
        else:
            sys.exit()


# 1. With the first message, the program should ask for a
#    difficulty level:
#    1 - simple operations with numbers 2 - 9
#    2 - integral squares 11 - 29
def main():
    exam = ArithmeticExamApplication()
    exam.start()


if __name__ == '__main__':
    main()
