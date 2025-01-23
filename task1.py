# Quiz questions and answers
questions = [
    "What is the capital of France?",
    "What is 2 + 2?",
    "What is the color of the sky on a clear day?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbols for steal?"
]

answers = [
    "Paris",
    "4",
    "Blue",
    "Jupiter",
    "H2O"
    "Fe"
]

# Initialize score
score = 0

# Function to conduct the quiz
def conduct_quiz():
    global score
    total_questions = len(questions)
    
    # Loop through each question
    for i in range(total_questions):
        print(f"Question {i + 1}: {questions[i]}")
        user_answer = input("Your answer: ")
        
        # Check if the answer is correct
        if user_answer.strip().lower() == answers[i].strip().lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answers[i]}.\n")
    
    # Display the final score
    print(f"You got {score} out of {total_questions} questions correct.")
    percentage = (score / total_questions) * 100
    print(f"Your score percentage: {percentage:.2f}%")

# Start the quiz
if __name__ == "__main__":
    print("Welcome to the Quiz!")
    conduct_quiz()
    print("Thank you for playing the Quiz!")
    