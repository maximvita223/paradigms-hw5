def merge_sort(Array):
    if len(Array) == 1 or len(Array) == 0:
        return Array
    L = merge_sort(Array[:len(Array) // 2])
    R = merge_sort(Array[len(Array) // 2:])
    n = m = k = 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(Array)):
        Array[i] = C[i]
    return Array


list = [2,3,4,5,1,42,31,23,12,54,23,32,12,3,12,3,12,41,32,5,23,4412,23,12,3,15,23,4,233,2,41,3,12]

print(merge_sort(list))




def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    left = [x for x in numbers[1:] if x < pivot]
    right = [x for x in numbers[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

list2 = [2,3,4,5,1,42,31,23,12,54,23,32,12,3,12,3,12,41,32,5,23,4412,23,12,3,15,23,4,233,2,41,3,12]

print(quick_sort(list2))