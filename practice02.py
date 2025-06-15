def calculate_age(birth_year: int, current_year=2025):      # hozirgi yilning current_year qilib taminlab oldik 
    """ Foydalanuvchini tug'ulgan sanasini anig'lab beardi.
    Bu functionda foydalanuvchi faqatgina uzini tug'ulgan yilini kiritadi va dastur foydalanuvchidan hozirgi yilni kiritishini suramaydi
    bunda hozigi yilimz argumentda tamminlangan buladi: Foydalanuvchi hozirgi yilni kiritmaydi tizim avtomatik hisoblydi' 
    Args:
        birt_year (int): bu argument qiymat qabul qiladi
        current_year(int): Bu argument hozirgi yil bilan taminlangan
    Returns:
        int: The sum of "birt_year" and "current_year"
    Raises:
        TypeError: Notug'ri turdagi qiymat
        SyntaxError: Notug'ri yozilgan kod.."""
    result = current_year - birth_year
    return result

def main():
    # foydalanuvchi faqatgina uzini tug'ulgan yilini kiritadi va dastur foydalanuvchidan hozirgi yilni kiritishini suramaydi  

    birth_year = int(input("Tug'ilgan yilingizni kiriting: "))
    c = calculate_age(birth_year)                 
    print(c)
  # agar balog'at yoshiga yetgan bo'lsa  "siz balog'atga yetgansz" or "siz balog'atga yetmagansz" deb chiqaradi.
    if c >= 18:
        print("siz balog'atga yetgansz ")
    else:
        print("siz balog'atga yetmagansz")
    
main()






