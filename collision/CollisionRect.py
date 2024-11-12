def isCollisionRect(list1,list2):
    id_exc= 0
    correct_error = False


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
        all_points_list1=[(i,j) for i in range(int(numX1),int(numX2)+1) for j in range(int(numY1),int(numY2)+1)]  #Список для всего поля 1 прямоугольника
        all_points_list2=[(i,j) for i in range(int(numX3),int(numX4)+1) for j in range(int(numY3),int(numY4)+1)]  #Список для всего поля 2 прямоугольника
        print(all_points_list1)
        print(all_points_list2)
        if (list2[0] in all_points_list1  or  list2[1] in all_points_list1) or (list1[0] in all_points_list2  or  list1[1] in all_points_list2) :  #Проверка нахождения 1 прямоугольника во 2 или наоборот
            return True
        else:
            return False


         
         
