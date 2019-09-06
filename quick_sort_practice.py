"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    p = len(array) - 1
    if p == 0:
        return array
    else:
        print(array[p])
        i = 0
        while i < p:
            # print("Iter: ", i, "->", array[i])
            # print("p:", p, "=", array[p])
            # print(array)
            # print(array[i], array[p])
            if array[i] > array[p]:
                temp = array[i]
                array[i] = array[p-1]
                array[p-1] = array[p]
                array[p] = temp
                p -= 1
            else:
                i += 1
            print("p:", p, "=", array[p])
            print(array)
            
        if p == 0:
            print("q")
            # high_array = quicksort(array[p+1:])
            # return [array[p]] + high_array
            return [array[p]] + quicksort(array[p+1:])
        elif p == len(array) + 1:
            print("qq")
            return quicksort(array[0:p]) + [array[p]]
            # return [quicksort(array[0:p])] + [array[p]]
        else:
            print("qqq")
            # return quicksort(array[0:p-1]).extend(array[p]).extend(quicksort(array[p+1:]))
            # return quicksort(array[0:p-1]).append(array[p]).extend(quicksort(array[p+1:])) + [array[p]] + quicksort(array[p+1:])
            # return quicksort([array[p]])
            # print array[0:p]
            # return quicksort(array[0:p]) + [array[p]]
            # return type(quicksort(array[0:p]))
            # return [array[p]] + quicksort(array[p+1:])
            # low_array = quicksort(array[0:p])
            # return low_array + [array[p]]
            return quicksort(array[0:p]) + [array[p]] + quicksort(array[p+1:])
            
        # return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test = [2, 4, 1, 3]
print quicksort(test)
