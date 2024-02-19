def print_question(n1, op, n2):
    question = print(f"\n{n1} {op} {n2} = ?")
    return(question)

def answer_feedback(user_answer, correct_answer):
    print(f"Your answer was {user_answer}.")
    print(f"The correct answer is {correct_answer}.")

n1 = 10
n2 = 5

user_name = input("Please, insert your name: ")

print(f"Hi {user_name}! Welcome to the math quiz.")
print(f"{user_name}, can you answer the following questions?")

print_question(n1, "+", n2)
user_answer = input()
correct_answer = n1 + n2
answer_feedback(user_answer, correct_answer)

print_question(n1, "-", n2)
user_answer = input()
correct_answer = n1 - n2
answer_feedback(user_answer, correct_answer)

print_question(n1, "*", n2)
user_answer = input()
correct_answer = n1 * n2
answer_feedback(user_answer, correct_answer)

print_question(n1, "/", n2)
user_answer = input()
correct_answer = int(n1 / n2)
answer_feedback(user_answer, correct_answer)