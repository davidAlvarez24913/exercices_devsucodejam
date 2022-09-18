# 1. Let’s start …
# Look at this series: 7, 6, 8, 4, 9, 2, 10, 0, 11, -2, …
# Create a function that receives two integers: x and y. If any of them are 0 or negative, or if
# they are greater than 255, the function should return -1
# Otherwise, the function should return the sum of the x and y elements of the series.
# For example: If the function receives x = 1, y = 3, it should return: 15. 
# (Because the sum of the first plus the third argument is 7+8=15). 
# If the function receives x = 8, y = 9, it should return 11.
# (Because the sum of the 8th plus the 9th element is 0+11=11).
# The function will receive 2 integers, return an integer.
# David Avarez C

def exercise_1(x, y):
    mayor = 0
    serie =[7,6]
    
    if x <0  or y < 0 or y>255 or x> 255:
        print('Los parametros deben estar dentro del domino establecido')
        return -1
    else:
        if x > y:
            mayor = x
        else:
            mayor =y
        for i in range(mayor):
            if i%2 ==0:
                serie.append(serie[-2]+1)
            else:
                serie.append(serie[-2]-2)
    return serie[x-1] + serie[y-1]

if __name__ == '__main__':
    print(exercise_1(1,3))
    print(exercise_1(8, 9))
    print(exercise_1(-8, 9))


    
