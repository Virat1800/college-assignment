import random

def ask_question():
    # Generate two random numbers
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    
    # Randomly select an operation
    operation = random.choice(['+', '-', '*'])
    
    # Construct the question based on the selected operation
    if operation == '+':
        answer = num1 + num2
        question = f"What is {num1} + {num2}?"
    elif operation == '-':
        answer = num1 - num2
        question = f"What is {num1} - {num2}?"
    else:
        answer = num1 * num2
        question = f"What is {num1} * {num2}?"
    
    return question, answer

def quiz_game():
    score = 0
    num_questions = 5  # You can adjust the number of questions
    print("Welcome to the Math Quiz Game!")
    
    # Ask a series of questions
    for _ in range(num_questions):
        question, correct_answer = ask_question()
        print(question)
        
        # Get the user's answer
        user_answer = int(input("Your answer: "))
        
        # Check if the answer is correct
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    
    # Display the final score
    print(f"Your final score is: {score}/{num_questions}")

if __name__ == "__main__":
    quiz_game()
