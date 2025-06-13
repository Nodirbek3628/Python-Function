def calculate_age(birth_year, current_year=2025):           # hozirgi yilning current_year qilib taminlab oldik 
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






