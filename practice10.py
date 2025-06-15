    #Parolni kiritadi, kuchli yoki kuchsizligini tekshiradi (masalan, uzunligi 8 dan katta bo‘lsa kuchli)
def is_strong_password(password: str):
    """ Parol kuchini baholaydi..
    Args:
        password (str): Foydalanuvchi kiritgan parol.
    Returns:
        None: Natijani ekranga chiqaradi.
    Errors:
        TypeError: Agar password str bo'lmasa
    """
    if len(password)>=8:
        print("Kuchli parol:")
    elif len(password) < 8:
        print("kuchsiz parol: ")
    elif len(password) < 4:
        print("Eng kamida 4 ta belgi bo'lsn")
    
def main():
    pasword = input("Parolni kiriting:")

    is_strong_password(pasword)

main()

    
    
    
    


    

