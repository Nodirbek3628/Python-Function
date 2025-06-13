                               #Simple Grading System
def get_grade(score):           #Foydalanuvchi ball kiritadi → `A`, `B`, `C`, `F` baho qaytadi

    if 85 <= score <= 100:
        print("A")
    elif 75 <= score < 85:
        print("B")
    elif  60 <= score < 75:
        print("C")
    else:
        print("F")
def main():
    ball = int(input("Ballni kiriting (0-100) "))
    get_grade(ball)
    
main()