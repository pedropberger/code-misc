    def median(array):
        sorted_array = sorted(array)
        array_length = len(array)
        if array_length % 2 == 0: 
            return (sorted_array[array_length//2-1] + sorted_array[array_length//2]) / 2
        if array_length % 2 == 1:
            return sorted_array[array_length//2]
    n = len(arr)
    arr.sort()
    med = median(arr)
    m = n // 2
    if n % 2 == 0:
        q1 = median(arr[0:m])
        q3 = median(arr[m::])
    elif n % 2 == 1:
        q1 = median(arr[0:m])
        q3 = median(arr[m+1::])
    return [int(q1),int(med),int(q3)]
