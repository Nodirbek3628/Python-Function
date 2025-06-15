def is_valid_phone_number(phone: str):        #Telefon raqam 9 ta raqamdan iboratligini tekshiradi
    """ Telefon raqam 9 xonali raqamdan iboratligini tekshiradi.
    Args:
        phone (str): Foydalanuvchidan kiritilgan telefon raqam (matn ko'rinishida).
    Returns:
        bool: True agar faqat raqamlardan iborat va uzunligi 9 bo'lsa, aks holda False.

    Errors:
        None (lekin noto'g'ri input bo'lsa False qaytadi)
    """
    return phone.isdigit() and len(phone) == 9

raqam = input("Telefon nomer kiriting (9 xonalik): ")

if is_valid_phone_number(raqam):
    print("Telefon raqam to'g'ri ")
else:
    print("Telefon raqam notug'ri ")

print(raqam)