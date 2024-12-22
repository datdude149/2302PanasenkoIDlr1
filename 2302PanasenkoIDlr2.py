import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def insertion_sort_timsort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def timsort(arr):
    min_run = 32
    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_timsort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merged_array = merge(arr[left:mid + 1], arr[mid + 1:right + 1])
                arr[left:left + len(merged_array)] = merged_array
        size *= 2

def introsort(arr):
    def introsort_util(arr, begin, end, depth_limit):
        size = end - begin
        if size < 16:
            insertion_sort(arr[begin:end])
            return
        if depth_limit == 0:
            arr[begin:end] = sorted(arr[begin:end])
            return

        pivot = partition(arr, begin, end)
        introsort_util(arr, begin, pivot, depth_limit - 1)
        introsort_util(arr, pivot + 1, end, depth_limit - 1)

    def partition(arr, begin, end):
        pivot = arr[begin]
        i = begin + 1
        for j in range(begin + 1, end):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[begin], arr[i - 1] = arr[i - 1], arr[begin]
        return i - 1

    depth_limit = (len(arr).bit_length() - 1)
    introsort_util(arr, 0, len(arr), depth_limit)

def time_sorting_algorithm(alg, arr):
    start_time = time.time()
    alg(arr.copy())
    end_time = time.time()
    return end_time - start_time

n = 100
sorted_array = np.arange(n)
almost_sorted_array = np.arange(n)
almost_sorted_array[-10:] = np.random.permutation(almost_sorted_array[-10:])
reverse_sorted_array = np.arange(n, 0, -1)
random_array = np.random.randint(0, 1000, size=n)

results = {
    'Algorithm': [],
    'Sorted Time': [],
    'Almost Sorted Time': [],
    'Reverse Sorted Time': [],
    'Random Time': []
}

algorithms = [
    selection_sort, insertion_sort, bubble_sort, merge_sort,
    quick_sort, shell_sort, heap_sort, timsort, introsort
]

for alg in algorithms:
    results['Algorithm'].append(alg.__name__)
    sorted_times = []
    almost_sorted_times = []
    reverse_sorted_times = []
    random_times = []

    for _ in range(100):  
        sorted_times.append(time_sorting_algorithm(alg, sorted_array))
        almost_sorted_times.append(time_sorting_algorithm(alg, almost_sorted_array))
        reverse_sorted_times.append(time_sorting_algorithm(alg, reverse_sorted_array))
        random_times.append(time_sorting_algorithm(alg, random_array))

    results['Sorted Time'].append(np.mean(sorted_times))
    results['Almost Sorted Time'].append(np.mean(almost_sorted_times))
    results['Reverse Sorted Time'].append(np.mean(reverse_sorted_times))
    results['Random Time'].append(np.mean(random_times))

def linear_func(x, a, b):
    return a * x + b

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

plt.figure(figsize=(12, 8))

for col in ['Sorted Time', 'Almost Sorted Time', 'Reverse Sorted Time', 'Random Time']:
    times = results[col]
    x = np.arange(1, len(results['Algorithm']) + 1)

    try:
        popt, _ = curve_fit(quadratic_func, x, times)
        fit_y = quadratic_func(x, *popt)
        plt.plot(x, fit_y, linestyle='--', label=f'{col} Regression: {popt[0]:.4f}x^2 + {popt[1]:.4f}x + {popt[2]:.4f}')
    except Exception as e:
        print(f"Error fitting curve for {col}: {e}")

    plt.plot(x, np.array(times), marker='o', label=col)

plt.xticks(np.arange(1, len(results['Algorithm']) + 1), results['Algorithm'], rotation=45)
plt.xlabel('Sorting Algorithms')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Timing Comparison with Regression Curves')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

for i in range(len(results['Algorithm'])):
    print(f"{results['Algorithm'][i]} | "
          f"{results['Sorted Time'][i]:.6f} | "
          f"{results['Almost Sorted Time'][i]:.6f} | "
          f"{results['Reverse Sorted Time'][i]:.6f} | "
          f"{results['Random Time'][i]:.6f}")