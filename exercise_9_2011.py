# . The power of two
# Given a positive integer number determine if it’s the power of two of another integer.
# Don’t start coding, read the limitations.
# For example:
# If the function receives 25, it should return TRUE, because 5^2 = 25
# If the function receives 1, it should return TRUE, because 1^2 = 1
# If the function receives 16, it should return TRUE, because 4^2 = 16
# If the function receives 14, it should return FALSE.
# Limitation: You CAN’T use functions of square roots (sqrt() or similar), potentiation (pow() or
# similar). ONLY the basic arithmetic operations (sum, substraction, multiplication, division),
# and any logic operations are allowed.
# The function receives a positive integer greater than 0, and should return a boolean value.
# David Alvarez C

def exercise_9(num):
    if num>0 and num<=255:
        x = num/2
        while True:
            if x*x == num:
                return num
            else:
                copia_x = x
                x = (x + (num/x)) /2
                # print(x)
            if x == copia_x:
                break
        return x
    else:
        return 'the number does not have an exact square root'
if  __name__ == '__main__':
    print(exercise_9(17))