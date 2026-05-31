def selectionSort(array):
    size = len(array)

    # Find the smallest number
    for i in range(size):
        smallest = i
        # Each time we find the smallest, we swap it,
        # move forward one index, and find the next smallest
        for j in range(i + 1, size):
            if array[j] < array[smallest]:
                smallest = j
        
        # Swap the smallest with the left-most unswapped number
        array[smallest], array[i] = array[i], array[smallest]
    
    return array