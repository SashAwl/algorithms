from random import randint

def binarySearch(array, value, startPoint, endPoint):
    
    pivot = (startPoint + endPoint)//2
    
    if value < array[pivot]:
        return binarySearch(array, value, startPoint, pivot)
    elif value == array[pivot]:
        return pivot
    else:
        return binarySearch(array, value, pivot, endPoint)

arr = [3,4,5,6,7,8,51]
#for i in range(10):
    #arr.append(randint(0,20))
print(arr)
print('Search element index', binarySearch(arr, 9, 0, len(arr)))