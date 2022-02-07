




import math
import re

def easy_operat(a, b, operat):
    global result
    if operat.find('+') != -1:
            result = (a + b)
    elif operat.find('-') != -1:
            result = (a - b)
    elif operat.find('*') != -1:
            result = (a * b)
    elif operat.find('/') != -1:
        if b == 0:
            print('Ошибка! Деление на ноль!')
        elif operat.find('/') != -1:
            result = (a / b)
    return result
def hard_operat(a, operat):
    global result
    if operat.find('sin')!= -1:
        a = math.radians(a)
        result = math.sin(a)            
    elif operat.find('cos') != -1:
        a = math.radians(a)
        result = math.cos(a)      
    elif operat.find('tan') != -1:
        a = math.radians(a)
        result = math.tan(a)
    return result

print('   Добро пожаловать в калькулятор!')
q = "y"
while q == "y":    
    print('Введите данные для вычисления', end = " ")
    operat = str(input() )
    a, b = re.split("\+|\*|/|-|sin|cos|tan", operat)         
    
    if (not(a.isdigit())) and (not(b.isdigit())) :
        print("ВВЕДИТЕ КОРЕКТНОЕ ВЫРАЖЕНИЕ!!!")
        continue
    elif b == '':
        float(a)
        hard_operat(a, operat)    
    else:  
        a = float(a)
        b = float(b)
        easy_operat(a, b, operat)
    print(result)
    
    while True:
        print('Хотите выполнить еще вычисление? "y/n" или "c" \nдля продолжение вычисления с результатом')
        q = str(input())
        if q == 'n':
            print('Досвидания!')
            break
        elif q == 'y':
            break
        elif q == 'c':
            print('"',result,'"', end = "")
            operat = str(input())
            a, b = re.split("\+|\*|/|-|sin|cos|tan", operat)
            if b == '':            
                hard_operat(result, operat)
                print(result)
                continue
            else:
                b = float(b)
                easy_operat(result, b, operat)
                print(result)
                continue
    
        



#exec("a =" + input() + "\nprint(a)")