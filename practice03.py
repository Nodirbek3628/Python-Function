def is_even(number):    # biz birinchi qasi son juft qaysi son toq bolishini solishtirib oldk.
    result = number % 2 == 0
    return result
def print_even_message(number):
    if is_even(number):
        print(f"{number} - juft son. ")
    else:
        print(f"{number} — toq son. ")           #Even/Odd Number Checker**
                                      
def main():                            # Son kiritiladi, u **juft yoki toq**ligini aniqlaydi.
    num = int(input("Biror Sonni kiriting: "))       
    print_even_message(num)

main()

