# 11. Counter
# Given an array of integers, find which is repeated more times. Return the number that has
# more repetitions. If two numbers has the same amount of repetitions, return the lower
# number.
# For example, given this array:
# A = [1, 5, 3, -2, 4, 2, 4, -2, 5, 5, 2, 1, 3]
# 1 is repeated 2 times
# 5 is repeated 3 times
# 3 is repeated 2 times
# -2 is once
# 4 is repeated 2 times
# 2 is repeated 2 times
# The most repeated number is 5. The function should return: 5. (Because 5 is repeated 3
#                                                                times in the array).
# The function will receive an array of integers and return an integer.
# David Alvarez C

from timeit import repeat

# primera solucion solo usando conceptos de python
def exercise_11(my_array):
    uniques = set(my_array)
    list_out = [[list(filter(lambda i: i == x, my_array))[0], len(
        list(filter(lambda i: i == x, my_array)))] for x in uniques]
    # print(list_out)
    repeat_num = max([_[1] for _ in list_out])
    aux = list( filter( lambda k: k[1] == repeat_num , list_out))
    # print(aux)
    return aux[0]

# segunda solucion
# se puede hacer un conteo manual en un for


def exercise_11_v2(my_array):
    uniques = set(my_array)
    aux = []
    for x in my_array:
        count = 0
        if x in uniques:
            count +=1
        aux.append([x,count])
    print(aux)
    return 'version2'
if __name__ == '__main__':
    # print(exercise_11([1, 5, 3, -2, 4, 2, 4, -2, 5, 5, 2, 1, 3, -10, -10, -10, -10, -10, -10, -10, -10, -10]))
    print(exercise_11_v2([1, 5, 3, -2, 4, 2, 4, -2, 5, 5, 2, 1, 3]))
