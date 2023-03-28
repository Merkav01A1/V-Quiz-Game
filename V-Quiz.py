import random
from hist_questions import questions as hist_questions
from geo_questions import questions as geo_questions
from scie_questions import questions as scie_questions
from math_questions import questions as math_questions
from SF_questions import questions as sf_questions
from fin_questions import questions as fin_questions
from vio_questions import questions as vio_questions

# define the categories
categories = ["History", "Geography", "Science", "Mathematics", "Science Fiction", "Finland", "Violetverse"]

# define the difficulty levels
levels = ["easy", "medium", "hard"]

# create a dictionary that maps each category to its questions
questions = {
    "History": hist_questions,
    "Geography": geo_questions,
    "Science": scie_questions,
    "Mathematics": math_questions,
    "Science Fiction": sf_questions,
    "Finland": fin_questions,
    "Violetverse": vio_questions
}

# set the number of questions and the starting stage
num_questions = 9

# initialize the score
score = 0

def get_difficulty_level(i):
    easy_stage = 0
    medium_stage = num_questions//3
    hard_stage = num_questions*2//3
    if i in [easy_stage, medium_stage, hard_stage]:
        print(f"Level: {get_difficulty_level(i + 1).upper()}")
    if i < medium_stage:
        return "easy"
    elif i < hard_stage:
        return "medium"
    else:
        return "hard"


def choose_mode():
    print("Select a mode:")
    print("1. Single category")
    print("2. Mixed categories")
    mode_choice = input("Enter your choice: ")
    while mode_choice not in ["1", "2"]:
        print("Invalid choice. Please choose again.")
        mode_choice = input("Enter your choice: ")
    if mode_choice == "1":
        print("Choose a category:")
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category}")
        category_choice = input("Enter your choice: ")
        while category_choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Please choose again.")
            category_choice = input("Enter your choice: ")
        category = categories[int(category_choice) - 1]
        return [category]
    else:
        return categories


def get_category_choice(i):
    # randomly select two categories
    category1, category2 = random.sample(categories, 2)

    print(f"Question {i + 1}: Choose a category:")
    # prompt the user to choose a category
    print(f"1. {category1}")
    print(f"2. {category2}")
    category_choice = input("Enter your choice: ")

    # make sure the category choice is valid
    while category_choice not in ["1", "2"]:
        print("Invalid choice. Please choose again.")
        category_choice = input("Enter your choice: ")

    # assign the selected category based on the user's choice
    if category_choice == "1":
        category = category1
    else:
        category = category2

    return category


def get_question(category, level):
    # select a random question from the chosen category and level
    question = random.choice(questions[category][level])

    # print the question and options
    print(question["question"])
    random.shuffle(question["options"])
    for j, option in enumerate(question["options"]):
        print(f"{chr(j+65)}. {option}")

    return question


def get_answer():
    # get the answer from the user
    user_answer = input("Enter your answer: ").upper()

    return user_answer


def check_answer(question, user_answer):
    valid_choices = ['A', 'B', 'C', 'D']
    correct_answer_index = question["options"].index(question["answer"])
    correct_answer = chr(65 + correct_answer_index)
    while user_answer not in valid_choices:
        print("Invalid answer. Please enter a valid choice (A, B, C, or D).")
        user_answer = input("Your answer: ").upper()
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect! The correct answer is {question['answer']}.")
        return 0


def run_quiz(categories):
    score = 0
    # ask n questions
    for i in range(num_questions):
        # select the difficulty level
        level = get_difficulty_level(i)

        # get the category from the user
        if len(categories) == 1:
            category = categories[0]
        else:
            category = get_category_choice(i)

        # get the question and answer from the user
        question = get_question(category, level)
        answer = get_answer()

        # check the answer and update the score
        score += check_answer(question, answer)

    print(f"Your final score is {score} out of {num_questions}.")


def main():
    print("Welcome to the Quiz Game!")
    categories = choose_mode()
    run_quiz(categories)
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
