def check_guess(secret, guess):
  result = secret == guess
  return result

def print_result(is_correct):
  if is_correct:
    print("siz to'g'ri topdingiz: ")
  else:
    print(f"Afsus siz topa olmadz sirli son {secret} ")


secret = 75  # kompyuter uchun sirli son.
guess = int(input("Sirli sonni kiriting:"))

is_correct = check_guess(secret,guess)
print_result(is_correct)