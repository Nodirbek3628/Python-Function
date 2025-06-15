def c_to_f(celsius):              #Celsius ↔ Fahrenheit aylantirish
    """ Celsius'dan Fahrenheit'ga aylantiradi.
    Args:
        celsius (float): Harorat Celsius gradusida.
    Returns:
        float: Fahrenheit gradusida harorat.
    Errors:
        TypeError: Agar celsius raqam bo'lmasa (masalan: matn, None)."""
    
    return 9/5*celsius+32         #Celsius'dan Fahrenheit'ga aylantiradi.

def f_to_c(fahrenheit):
    return 5/9*(fahrenheit-32)    #Fahrenheit'dan Celsius'ga aylantiradi


C = 25
F = 77
print(c_to_f(C))
print(f_to_c(F))