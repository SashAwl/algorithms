from random import randint

# quickSort(array, startPoint, endPoint)
#             array - сортируемый массив
#             startPoint - начало сортируемого участка массива
#             endPoint - конец сортируемого участка массива

def quickSort(array, startPoint, endPoint):
   
    
# midlPoint - пивот, опорный элемент
    
    midlPoint = array[(startPoint + endPoint)//2]
    leftPoint = startPoint
    rightPoint = endPoint
     

    while leftPoint <= rightPoint:
        
        # Ищем элемент, не меньший, чем пивот, слева от него  
        
        while array[leftPoint] < midlPoint:
            leftPoint+=1
            
        # Ищем элемент, не больший, чем пивот, справа от него  

        while array[rightPoint] > midlPoint:
            rightPoint-=1
            
        # В случае нахождения таковых, меняем их местами и переходим 
        # к проверке следующих элементов       

        if leftPoint <= rightPoint:
            if leftPoint < rightPoint:
                array[leftPoint], array[rightPoint] = array[rightPoint], array[leftPoint]
               
            leftPoint+=1
            rightPoint-=1            

    # После распределения элементов таким образом, что все элементы слева 
    # от текущего пивота меньше него, а справа - больше, переходим 
    # к аналогичной процедуре с левой и правой частями массива по отдельности
    
    if leftPoint <= endPoint:
        quickSort(array, leftPoint, endPoint)        
        
    if startPoint <= rightPoint:
        quickSort(array, startPoint, rightPoint)
    

# Тестируем функцию быстрой сортировки на произвольном массиве
arr = []                
for i in range(10):
    arr.append(randint(0,10))
print(arr)

quickSort(arr, 0, (len(arr)-1))
print(arr)
