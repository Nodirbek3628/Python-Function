def is_even(number:int):    # biz birinchi qasi son juft qaysi son toq bolishini solishtirib oldk.
    """ Juft soni aniqlaydigan Function 
    Bu functionda foydalanuvchi kiritgan sonni jufligini aniqlab beradi.
    Args:
        number(int): Foydalanuvchi tomonidan kiritilgan butun son.
    Returns:
        bool: Agar son juft bo‘lsa True, agar toq bo‘lsa False.
    Raises:
        TypeError: Notug'ri turdagi qiymat
        SyntaxError: .Notug'ri yozilgan kod.
    """
    result = number % 2 == 0
    return result
def print_even_message(number):
    """
    Sonning juft yoki toqligi haqida foydalanuvchiga xabar beradi.

    Berilgan sonni `is_even()` funksiyasi orqali tekshiradi va
    natijaga qarab ekranga quyidagi xabarni chiqaradi:
        - "<son> — juft son."
        - "<son> — toq son."

    Args:
        number (int): Foydalanuvchi kiritgan butun son.

    Returns:
        None: Faqat natijani `print()` orqali chiqaradi.
    """
    if is_even(number):
        print(f"{number} - juft son. ")
    else:
        print(f"{number} — toq son. ")           #Even/Odd Number Checker**
                                      
def main():
    """ Dasturning asosiy boshqaruv funksiyasi.

    Foydalanuvchidan butun son qabul qiladi va uni `print_even_message()`
    funksiyasi yordamida juft yoki toqligini chiqaradi.

    Agar foydalanuvchi noto‘g‘ri ma’lumot (masalan: matn) kiritsa,
    `ValueError` xatoligini ushlab, foydalanuvchiga ogohlantiradi.

    Foydalanish:
        - Dastur ishga tushgach, foydalanuvchi son kiritadi.
        - Ekranda "juft" yoki "toq" degan natija chiqadi.

    Returns:
        None """
                              
    num = int(input("Biror Sonni kiriting: "))       
    print_even_message(num)

main()

