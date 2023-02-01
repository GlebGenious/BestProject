T = input("впиште градусы: ")
Degree = input("C либо F: ")
if Degree == "C":
    sha = 32 + (float(T) * (9/5))
    print("ответ в фарингейтах :" + (str(round(sha))))
elif Degree == "F":
    otvet = ((float(T) - 32) * (5/9))
    print("ответ в цельсиях :" + (str(round(otvet))))
