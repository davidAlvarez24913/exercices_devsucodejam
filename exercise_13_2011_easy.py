# 13. Something easy...
# You are given an array with positive and negative integers. Write a function to change the
# elements order in the array such that negative integers are at the beginning, the positive
# integers are at the end. Zero(0) and integers that have the same sign don't change order.
# For example, if the function receives:
# a[0] = 4
# a[1] = -3
# a[2] = -100
# a[3] = 7
# a[4] = 0
# a[5] = 1
# a[6] = -6
# the function should return:
# a[0] = -3
# a[1] = -100
# a[2] = -6
# a[3] = 4
# a[4] = 7
# a[5] = 0
# a[6] = 1
# The function receives an array of integers and return an array of integers.
# Limitations:
# You CAN’T use sorting methods provided by the language. (eg. Array.sort(), sort(), etc...). If
# you need to, you should create your own implementation of the sorting function.
# David Alvarez C.

def exercise_13(my_array):
    negative = []
    positive = []
    for x in my_array:
        if x <0 :
            negative.append(x)
        else:
            positive.append(x)
    result = negative + positive 
    return result

if  __name__ == '__main__':
    print(exercise_13([4,-3,-100,7,0,1,-6]))
    