#функция проверки на корректность ввода
def isCorrectRect(c):
    if c[0][0] < c[1][0] and c[0][1]< c[1][1]:
        return True
    else:
        return False


#Cбор данных
numX1=float(input('Введите значение для x1 '))
numY1=float(input('Введите значение для y1 '))
numX2=float(input('Введите значение для x2 '))
numY2=float(input('Введите значение для y2 '))

#Cоздание списка
num1 = [(numX1,numY1),(numX2,numY2)]


sef=isCorrectRect(num1)
print(sef)



