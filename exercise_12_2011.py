# 12. The last piece of cake
# Equilibrium index of a sequence is an index such that the sum of elements at lower indexes
# is equal to the sum of elements at higher indexes.
# Create a function that receives an array of integers and returns the first equilibrium index
# found. If no equilibrium index found, the function should return -1
# For example, if the array received is :
# A = [-7, 1, 5, 2, -4, 3, 0]
# 3 is an equilibrium index, because:
# A[0]+A[1]+A[2] = A[4]+A[5]+A[6]
# In other words, you should find the index of the array where the sum of the left elements is
# equal to the sum of the right elements.
# In the example, the function will return 3, because it’s the first equilibrium index found in the
# array.
# The function receives an array of integers and return an integer
# David Alvarez C


def exercise_12(my_array):
    def resolve(my_array):
        out = 0
        for count in range(len(my_array)):
            if sum(my_array[:count+1]) == sum(my_array[count+2:]):
                out = count+1
                return out
    aux = resolve(my_array)
    if aux == None:
        return -1
    else:
        return aux
if __name__ == '__main__':
    print(exercise_12([-7, 1, 5, 2, -4, 3, 0]))
    print(exercise_12([-3, 5, 100, 0, 4, 2, -4]))
    print(exercise_12([-3, -2, -100, 0, -100, -3, -2]))
    print(exercise_12([30, 120, 0, -5, -5, 30, 20, 100, 10]))
    print(exercise_12([-7, 11, 5, 2, -24, 3, 1]))
