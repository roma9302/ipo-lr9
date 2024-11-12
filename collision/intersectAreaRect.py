def intersectionAreaRect(list1,list2):

    id_exc= 0  #Переменная индекса ошибки
    correct_error = False  #Проверка на корректность ввода
    intersection=[]  #Список всех пересечений
    count_inter=0  #Площадь пересечения в клетках




#Класс  для нашей ошибки
    class RectCorrectError(Exception):
        pass



 
#обработка корректности ввода
    if  list1[0][0] >= list1[1][0] or list1[0][1] >= list1[1][1] :
        id_exc += 1
        correct_error =  True
    
    elif list2[0][0] >= list2[1][0] or list2[0][1]  >=  list2[1][1]:
        id_exc += 2 
        correct_error = True

#Вызов ошибки при некоррекитном вводе
    if correct_error :
            raise RectCorrectError(f'{id_exc}й прямоугольник некоректный')
    
    
#Нахождение пересеченеия
    elif correct_error == False:
        all_points_list1=[(i,j) for i in range(int(numX1),int(numX2)) for j in range(int(numY1),int(numY2))]  #Список для всего поля 1 прямоугольника
        all_points_list2=[(i,j) for i in range(int(numX3),int(numX4)) for j in range(int(numY3),int(numY4))]  #Список для всего поля 2 прямоугольника
        print(all_points_list1)
        print(all_points_list2)
        for i in range(len(all_points_list1)):
            for j in range(len(all_points_list2)):
                if  all_points_list1[i] == all_points_list2[j]:  #Проверка пересечений для двух прмямоугольников
                    intersection.append(all_points_list1[i])
                    count_inter+=1

        return count_inter
    else:                  #Возвращение значений
        return 0



        
