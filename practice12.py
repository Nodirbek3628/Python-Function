# Vazifa: Og‘irlik va bo‘y kiritiladi → BMI va uning holati chiqadi.

# Funksiya:

# calculate_bmi(weight: float, height: float) -> float
# bmi_status(bmi: float) -> str.
lang = "uzb"
def select_lang():
    global lang
    lang = input("tilni tanlang uz/eng >>>>")

def chek_lang():
    """Foydalanuvchidan tilni tanlashini so'raydi va global `lang` o'zgaruvchisini yangilaydi.
    Faqat 'uzb' yoki 'eng' tillarini qabul qiladi. Noto'g'ri kiritilsa, 'uzb' qilib o'rnatiladi
    """
    global lang
    lang = "eng"

def calculate_bmi(weight:float, height:float):
    """
    Tana massasi indeksini (BMI) hisoblaydi.

    Args:
    - weight (float): Tana vazni (kg).
    - height (float): Bo'y uzunligi (metrda).

    Returns:
    - float: BMI qiymati, 2 raqamgacha yaxlitlangan.
    """
    return round(weight / (height ** 2), 2)

def bmi_status(bmi):
    #  """ BMI qiymatiga qarab sog'liq holatini aniqlaydi.

    # Args:
    # - bmi (float): Tana massasi indeksi.

    # Return:
    # - str: BMI holati ('Ozg'in', 'Normal', 'Semiz' yoki 'Underweight', 'Normal', 'Overweight').
    # """
    if bmi < 18.5:
        return "Ozg'in"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Semiz"

def main():
    #   """ Dastur ishga tushganda bajariladigan asosiy funksiya.
    # Til tanlanadi, foydalanuvchidan vazn va bo'y olinadi,
    # BMI hisoblanadi va natija chiqariladi.
    # """
    select_lang()
    weight,height = None,None
    if lang == "eng":
        weight = float(input("enter weight (kg): "))
        height = float(input("height (m): "))
    elif lang == "uzb":
        weight = float(input("Vazningizni kiriting (kg): "))
        height = float(input("Bo'yingizni kiriting (metrlarda): "))
            
    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)
    if lang == "uzb":
        print(f"\nBMI: {bmi}")
        print(f"Holati: {status}")
    elif lang  == "eng":
        print(f"\nBMI: {bmi}")
        print(f"Status: {status}")
        
main()  
