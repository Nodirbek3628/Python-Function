def check_guess(secret, guess):
  """
    Foydalanuvchining taxmini sirli songa tengligini tekshiradi.

    Args:
        secret (int): Kompyuter tanlagan sirli son.
        guess (int): Foydalanuvchining kiritgan soni.

    Returns:
        bool: True agar to'g'ri topsa, aks holda False.

    Errors:
        TypeError: Agar 'secret' yoki 'guess' butun son (int) bo'lmasa.
    """
  return secret == guess


  result = secret == guess
  return result

def print_result(is_correct):
    # """ Natijani chop etadi: foydalanuvchi ' topdimi yoki yo'qmi.
    # Args:
    #     is_correct (bool): Taxmin ' bo'lsa True.
    #     secret (int): Sirli son, noto'g'ri bo'lsa foydalanuvchiga ko'rsatiladi.
    # Returns:
    #     None
    # Errors:
    #     TypeError: 'is_correct' boolean emas yoki 'secret' int bo'lmasa."""
  if is_correct:
    print("siz to'g'ri topdingiz: ")
  else:
    print(f"Afsus siz topa olmadz sirli son {secret} ")


secret = 75  # kompyuter uchun sirli son.
guess = int(input("Sirli sonni kiriting:"))

is_correct = check_guess(secret,guess)
print_result(is_correct)