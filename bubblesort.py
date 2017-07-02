n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def bubble_sort(array):
    numSwaps = 0

    if len(array) < 2:
        return numSwaps

    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
                numSwaps += 1

    return numSwaps

swaps = bubble_sort(a)

print('Array is sorted in {0} swaps.'.format(swaps))
print('First Element: {0}'.format(a[0]))
print('Last Element: {0}'.format(a[-1]))