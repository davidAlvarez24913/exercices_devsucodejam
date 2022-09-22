# 5. Just One Line
# Write a function to remove duplicates from a sorted array of integers. Pretty easy, right?
# What about making it in one line of code? (You can use as many statements as needed, but
#                                            the code should be written in one line).
# Example:
# If the function receives this array:
# A = [-3, -2, 0, 0, 5, 7, 9, 11, 11, 25]
# The function should return:
# A = [-3, -2, 0, 5, 7, 9, 11, 25]
# The function will receive an array of integers, and return an array of integers.
# # David Avarez C

def exercise_5(x):
    if isinstance(x, list) :
        return sorted(list(set(x))) 
    else:
        return 'Debe ingresar un array'

            
if __name__ == '__main__':
    print(exercise_5([-1,-1,0,1,2,2,4,6,8]))



    
