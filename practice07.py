def ask_question(question:str):         # Savol beriladi, javobni tekshiradi
    """ Foydalanuvchiga savol beradi va javobini qaytaradi
    Args:
        question (str): Foydalanuvchiga beriladigan savol matni.
    Returns:
        str: Foydalanuvchining javobi (qirqilgan).
    Errors:
        None (input noto'g'ri bo'lsa ham faqat string qaytariladi)..
    """
    user_answer = input(f"{question}").strip()
    return user_answer

def check_answer(user_answer:str, correct_answer:str):
    """
    Foydalanuvchining javobini to'g'ri javob bilan taqqoslaydi
    Args:
        user_answer (str): Foydalanuvchining javobi.
        correct_answer (str): To'g'ri javob.
    Returns:
        bool: True agar javob to'g'ri bo'lsa, aks holda False.
    Errors:
        TypeError: Agar argumentlar string bo'lmasa.
    """
    return user_answer.lower() == correct_answer.lower()

def main():
    """ Dastur bosh funksiyasi.
    Savol beriladi va foydalanuvchi javobi tekshiriladi.
    """
    question = "O'zbekiston poytaxti qayer?"
    correct_answer = "Toshkent"
    
    user_answer = ask_question(question)
    is_correct = check_answer(user_answer,correct_answer)

    if is_correct:
        print("to'g'ri topdingz")
    else:
        print(f"topa olmadz,to'g'ri javob \" {correct_answer}")
    
main()
