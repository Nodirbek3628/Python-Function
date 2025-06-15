                               #Simple Grading System
def get_grade(score:int):           #Foydalanuvchi ball kiritadi → `A`, `B`, `C`, `F` baho qaytadi
    #    """ Kiritilgan ball asosida baho chiqaradi.

    # Ball quyidagi oraliqlarga tushsa, mos ravishda baho beriladi:
    #     - 85-100 → A
    #     - 75-84  → B
    #     - 60-74  → C
    #     - 0-59   → F

    # Args:
    #     score (int): Foydalanuvchi tomonidan kiritilgan ball (0-100 oralig'ida).

    # Returns:
    #     None: Natijani `print()` orqali ekranga chiqaradi.

    # Raises:
    #     ValueError: Agar score manfiy bo'lsa yoki 100 dan katta bo'ls.
    #     TypeError: Agar score butun son (int) bo'lmasa
    # """
    if 85 <= score <= 100:
        print("A")
    elif 75 <= score < 85:
        print("B")
    elif  60 <= score < 75:
        print("C")
    else:
        print("F")
def main():
    """
    Dasturning bosh funksiyasi — foydalanuvchidan ball qabul qiladi
    va `get_grade()` funksiyasi orqali unga mos bahoni chiqaradi.

    Returns:
        None

    Raises:
        ValueError: Agar foydalanuvchi son o'rniga matn kiritsa.
    """
    ball = int(input("Ballni kiriting (0-100) "))
    get_grade(ball)
    
main()