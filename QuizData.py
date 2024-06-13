import random

# Quiz questions and answers
quiz_questions = {
    "Is the sky blue?": "true",
    "Is fire cold?": "false",
    "Do fish swim?": "true",
    "Is the earth flat?": "false",
    "Is water wet?": "true",
    "Can humans fly without aid?": "false",
    "Is the sun a star?": "true",
    "Is ice hot?": "false",
    "Can birds sing?": "true",
    "Is a slug's color green?": "true"
}

def run_quiz():
    # Select 4 random questions from the quiz data
    questions = random.sample(list(quiz_questions.items()), 4)

    score = 0
    total_questions_asked = 0

    for i, (question, correct_answer) in enumerate(questions, 1):
        # Ask the user the question
        user_answer = input(f"Question {i}: {question} (true or false): ").strip().lower()

        # Check the answer and provide feedback
        total_questions_asked = i
        if user_answer == correct_answer:
            print("You got it right!")
            score += 1
            print(f"Current score: {score}/{total_questions_asked}")
            print()
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer.capitalize()}")
            print(f"Final score: {score}/{total_questions_asked}")
            return

    # Display the final score if all answers were correct
    print(f"Your final score is: {score}/{total_questions_asked}")
    print(f"Congratulations ! You won 100 Bucks :) ")

# Run the quiz
if __name__ == "__main__":
    run_quiz()