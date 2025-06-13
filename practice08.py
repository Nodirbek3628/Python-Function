def c_to_f(celsius):              #Celsius ↔ Fahrenheit aylantirish
    return 9/5*celsius+32         #Celsius'dan Fahrenheit'ga aylantiradi.

def f_to_c(fahrenheit):
    return 5/9*(fahrenheit-32)    #Fahrenheit'dan Celsius'ga aylantiradi


C = 25
F = 77
print(c_to_f(C))
print(f_to_c(F))