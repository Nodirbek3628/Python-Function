def check_guess(secret,guess):                 #Number Guessing Game (Random ishlatilmaydi)
    return secret == guess
def print_result(is_correct):
    if is_correct:
        print("To'g'ri topdingiz ")
    else:
        print("Xato topdingiz ")
secret = 7    # Sirli sonni o‘zgaruvchi sifatida beramiz (masalan, 7)

guess = int(input("taxmin soningizni kiriting (0-10)"))

a = check_guess(secret,guess)
print_result(a)