# 10. Perfect numbers
# A perfect number is a positive integer that is equal to the sum of its proper divisors. Fore 6 = 1+2+3.
# example, 6 is a perfect number becaus
# Create a function that receives two values X and Y and return the smaller perfect number
# found, which is greater or equal than X and lower or equal than Y. If no perfect number
# found, it should return -1.
# For example, if the function receives X = 5, Y = 7, it should return 6, because 6 is the smaller
# perfect number between 5 and 7.
# The function will receive two integers and return one integer.
# David Alvarez C


def exercise_10(num_a,num_b):
    def perfect(n):
            aux = [x for x in range(1,n) if n % x == 0]
            if sum(aux) == n:
                return n
            else:
                return -1
            
    list_domain = list(range(num_a, num_b))
    list_perfect = list(filter( lambda x: x>0 ,[perfect(_) for _ in list_domain ]))
    return min(list_perfect)

if __name__ == '__name__':
    print(exercise_10(5,36))
