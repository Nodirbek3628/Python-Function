
def add(a: int, b: int):
    """ Ikki sonning yig'indisini topish 

    bu function ikki sonning yig'indisini topishda keng qullaniladi.

    Args:
        a (int): a qiymat qabul qiladi.
        b (int): b qiymat qabul qiladi.
    Returns:
        int: a va b ning yig'indisining chiqarib beradi.
    Raises:
        AnyError:
        ValueError: integerg string qiymat berganimizda chiqadigan xato.
    """
    result = a + b
    return result

def subtract(a: int, b: int):
    """ Ikki sonning ayirmasioni  topish 

    bu function ikki sonning ayirmasini sini topishda keng qullaniladi.

    Args:
        a (int): a qiymat qabul qiladi.
        b (int): b qiymat qabul qiladi.
    Returns:
        int: a va b ning ayirmasini  chiqarib beradi.
    Raises:
        AnyError:
        ValueError: integerg string qiymat berganimizda chiqadigan xato.
    """
    result = a - b
    return result

def multiply(a: int, b: int):
    """ Ikki sonning ko'paytmasini  topish 

    bu function ikki sonning ko'paytmasini  topishda keng qullaniladi.

    Args:
        a (int): a qiymat qabul qiladi.
        b (int): b qiymat qabul qiladi.
    Returns:
        int: a va b ning ko'paytmasining chiqarib beradi.
    Raises:
        AnyError:
        TypeError: Notug'ri turdagi qiymat
        ValueError: integerga string qiymat berganimizda chiqadigan xato.
    """
    result = a * b
    return result

def divide(a: int, b: int):
    """ Ikki sonning bulinmasini  topish 

    bu function ikki sonning bulinmasini  topishda keng qullaniladi.

    Args:
        a (int): a qiymat qabul qiladi.
        b (int): b qiymat qabul qiladi.
    Returns:
        int: a va b ning bulinmani  chiqarib beradi.
    Raises:
        AnyError:
        ValueError: integerg string qiymat berganimizda chiqadigan xato.
        TypeError: Notug'ri turdagi qiymat.
    """
    result = a / b
    return result

def main():
    a = int(input("a= "))
    op = input("ishora kiriting (+,-,*,/)")
    b = int(input("b= "))

    if op == "+":
        print(add(a,b))
    elif op == "-":
        print(subtract(a,b))
    elif op == "*":
        print(multiply(a,b))
    elif op == "/":
        print(divide(a,b))
    else:
        print("wrong operator")

main()