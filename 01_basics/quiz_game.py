questions = {
    "What is the capital of India? ": "delhi",
    "What is 5 + 5? ": "10",
    "Which language are we learning? ": "python"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question).lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Your score:", score, "/", len(questions))