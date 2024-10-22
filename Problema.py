import time
import random
import numpy as np

def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Function to find the partition position
def partition(arr, low, high):

    # choose the rightmost element as pivot
    pivot = arr[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (arr[i], arr[j]) = (arr[j], arr[i])

    # Swap the pivot element with the greater element specified by i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort
def quickSort(arr, low, high):
    start = time.time()
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr, low, high)

        # Recursive call on the left of pivot
        quickSort(arr, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(arr, pi + 1, high)
    end = time.time()
    execution = end - start
    print("Se ejecuto quickSort en ", execution, " nano segundos")

def prueba_bubble(size, index = 10):
    lista = []
    for _ in range(index):
        arr = [random.randint(0,size) for _ in range(size)]
        start_time = time.time()
        bubble_sort(arr)
        #print("entro a bubble")
        end_time = time.time()
        lista.append(end_time - start_time)
    return np.mean(lista)
    lista = []

def prueba_quick(size, index = 10):
    lista = []
    for _ in range(index):
        arr = [random.randint(0,size) for _ in range(size)]
        start_time = time.time()
        quickSort(arr, low=0, high = size - 1)
        print("entro a quick")
        end_time = time.time()
        lista.append(end_time - start_time)
    return np.mean(lista)
    lista = []

sizes = [1000, 2000, 3000, 4000, 5000]

for size in sizes:
    avg = prueba_bubble(size)
    print(f"Tiempo promedio de ejecucion bubble sort con tamano {size}: {avg:.5f} segundos")

for size in sizes:
    avg = prueba_quick(size)
    print(f"Tiempo promedio de ejecucion quick sort con tamano {size}: {avg:.5f} segundos")





