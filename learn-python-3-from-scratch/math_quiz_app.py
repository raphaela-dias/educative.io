import random

def greet_user(user_name):
    welcome_message = (f"Hello {user_name}! Welcome to the math quiz.\nYou will be provided with 5 questions, and each carries one mark.\nGood luck!")
    print(welcome_message)

def print_question(n1, op, n2):
    question = print(f"\n{n1} {op} {n2} = ?")
    return(question)

def answer_feedback(user_answer, correct_answer):
    print(f"Your answer was {user_answer}.")
    print(f"The correct answer is {correct_answer}.")

def farewell_user(user_name):
    farewell_message = (f"\nThanks for giving the quiz {user_name}; You will get your result soon.")
    print(farewell_message)

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
user_name = input("Please, insert your name: ")
greet_user(user_name)

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
print_question(n1, "+", n2)
user_answer = input()
correct_answer = n1 + n2
answer_feedback(user_answer, correct_answer)

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
print_question(n1, "-", n2)
user_answer = input()
correct_answer = n1 - n2
answer_feedback(user_answer, correct_answer)

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
print_question(n1, "*", n2)
user_answer = input()
correct_answer = n1 * n2
answer_feedback(user_answer, correct_answer)

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
print_question(n1, "/", n2)
user_answer = input()
correct_answer = int(n1 / n2)
answer_feedback(user_answer, correct_answer)

farewell_user(user_name)