# Bubble Sort HackerRank Challenge!

Here is a solution to the [Bubble Sort Coding Challenge](https://www.hackerrank.com/challenges/ctci-bubble-sort)

## The Challenge

We are given a prompt as follows:

```
Given an n-element array, A, of distinct elements, sort array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
First Element: firstElement, where firstElement is the first element in the sorted array.
Last Element: lastElement, where lastElement is the last element in the sorted array.
```

We are given a sample algorithm but I have chosen to write mine in Python.

So we know we will be tested with an array containing numbers that are not necessarily in the correct (ascending) order. We must write an algorithm that makes the array in correct order through swapping.  

## The Solution

The heart of this problem is creating a loop that runs through an array, compares adjascent elements, and swaps the elements such that the pair are placed in ascending order.  

We will start by creating a bubble_sort method that takes in an array:

```
def bubble_sort(array):
    numSwaps = 0

    if len(array) < 2:
        return numSwaps
```
In our method we define numSwaps as 0, this will be the variable used to keep track of the number of swaps that occur to correct the array. For a sanity check we throw in a short conditional that says if the length of the array is less than 2 then return numSwaps (0) - because we can't sort one element!

```
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
                numSwaps += 1

    return numSwaps

swaps = bubble_sort(a)
```

Now for the meat of the solution. Our alogrithm begins by iterating `i` using the Python function `range()`, in this example we run backwords through the array `range(len(array) - 1, 0, -1)` as a reminder this function takes in parameters where ours is Start (the length of the array -1 - or the last element in the array), Stop (at 0 - or the first element in the array), and Step (countdown with -1). 

Four elements in each step, if the element is greater than the element next to it (or in a index position + 1 from it), we perform a swap and add 1 to our numSwaps varibale. 

We then return numSwaps and here we set the method/returned value as `swaps`

```
print('Array is sorted in {0} swaps.'.format(swaps))
print('First Element: {0}'.format(a[0]))
print('Last Element: {0}'.format(a[-1]))
```

As for our print statements, we give what the prompt asks for and use the `.format()` function to replace `{0}` with `numSwaps` (as passed through our `swaps` variable), the first element of our sorted array (at index 0), and the last item of our sorted array (at index -1).