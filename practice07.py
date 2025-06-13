def ask_question(question: str, correct_answer: str):         # Savol beriladi, javobni tekshiradi
    print(question)

    user_answer = input("Javobingizni kiriting: ")
    if check_answer(user_answer, correct_answer):
        print("To'g'ri javob!")
    else:
        print(f"Noto'g'ri. To'g'ri javob: {correct_answer}")

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()
