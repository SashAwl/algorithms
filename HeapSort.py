from random import randint

# heapify(array, n, i) - преобразует поддерево в двоичную кучу
#          array - сортируемый массив
#          n - размерность массива
#          i - индекс корневого узла

def heapify(array, n, i):
    largest = i 
    left = 2 * i + 1   
    right = 2 * i + 2   

  # Проверяем существует ли левый дочерний элемент больший, чем корень

    if left < n and array[i] < array[left]:
        largest = left

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if right < n and array[largest] < array[right]:
        largest = right

    # Заменяем корень, если нужно
    if largest != i:
        array[i],array[largest] = array[largest],array[i]

        # Применяем heapify к корню
        heapify(array, n, largest)

# heapSort(array) - сортирует массив заданного размера

def heapSort(array):
    n = len(array)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(array, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]  
        heapify(array, i, 0)

# Тестируем функцию пирамидальной сортировки на произвольном массиве
arr = []                
for i in range(10):
    arr.append(randint(0,10))
print(arr)

heapSort(arr)
print (arr)
