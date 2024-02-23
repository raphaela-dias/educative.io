########################
# IMPORTED LIBRARIES

import random

########################
# FUNCTION DEFINITIONS

def greet_user(user_name):
    welcome_message = (f"Hello {user_name}! Welcome to the math quiz.\nYou will be provided with 5 questions, and each carries one mark.\nGood luck!")
    print(welcome_message)

def print_question(n1, op, n2):
    question = print(f"\n{n1} {op} {n2} = ?")
    return(question)

def choose_operator(op_n):
    operator = op_n
    if operator == 1:
        return "-"
    elif operator == 2:
        return "+"
    elif operator == 3:
        return "*"
    else:
        return "/"

def calculate_answer(n1, operator, n2):
    if operator == "-":
        return n1 - n2
    elif operator == "+":
        return n1 + n2
    elif operator == "*":
        return n1 * n2
    else:
        return int(n1 / n2)

def answer_feedback(user_answer, correct_answer, points):
    if user_answer == correct_answer:
        print("Correct answer")
        points = points + 1
        return points
    else:
        print(f"Oops, that's not right.\nThe correct answer is {correct_answer}")
        return points

def farewell_user(user_name, points):
    farewell_message = (f"\nThanks for giving the quiz {user_name}.\nYour final score is {points}.")
    print(farewell_message)

########################
# PRESET VARIABLES

points = 0
counter = 0

########################
# MAIN STRUCTURE

user_name = input("Please, insert your name: ")
greet_user(user_name)

while counter < 4:

    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    operator = choose_operator(random.randint(1, 4))
    print_question(n1, operator, n2)
    user_answer = int(input())
    correct_answer = calculate_answer(n1, operator, n2)
    points = answer_feedback(user_answer, correct_answer, points)
    
    counter += 1

farewell_user(user_name, points)