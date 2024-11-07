from collision.CorrectRec import isCorrectRect
from collision.intersectAreaRect import intersectionAreaRect
from collision.CollisionRect import isCollisionRect
from collision.intersectAreaMultiRect import intersectionAreaMultiRect

def main():
    while True:

        number = int(input("Выбор: 1 - intersectionAreaRect , 2 - isCorrectRect , 3 - isCollisionRect , 4 - intersectionAreaMultiRect , 5 - Выход"))

        if number == 1:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            rect1 = [(x1, y1), (x2, y2)]

            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rect2 = [(x3, y3), (x4, y4)]
            print(intersectionAreaRect(rect1, rect2))


        elif number == 2:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            rect = [(x1, y1), (x2, y2)]
            print(isCorrectRect(rect))
              

        elif number == 3:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            rect1 = [(x1, y1), (x2, y2)]

            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rect2 = [(x3, y3), (x4, y4)]
            print(isCollisionRect(rect1, rect2))


        elif number == 4:
            n = int(input("Количество прямоугольников: "))
            rectangles = []

            for i in range(n):
                print(f"Прямоугольник {i + 1}:")
                x1 = float(input('Введите x1: '))
                y1 = float(input('Введите y1: '))
                x2 = float(input('Введите x2: '))
                y2 = float(input('Введите y2: '))
                rectangles.append([(x1, y1), (x2, y2)])
            print(intersectionAreaMultiRect(rectangles))

        elif number == 5:
            print("Выход")
            break
        else:
            print(f"Вы ввели {number} .Введите число от 1 до 5")

main()