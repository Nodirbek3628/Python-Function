def is_valid_phone_number(phone: str):        #Telefon raqam 9 ta raqamdan iboratligini tekshiradi
    return phone.isdigit() and len(phone) == 9

raqam = input("Telefon nomer kiriting (9 xonalik): ")

if is_valid_phone_number(raqam):
    print("Telefon raqam to'g'ri ")
else:
    print("Telefon raqam notug'ri ")

print(raqam)