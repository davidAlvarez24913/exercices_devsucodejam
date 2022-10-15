# 20. Come on, give me something challenging man!
# From Wikipedia:
# In number theory, a partition of a positive integer n, also called an integer partition, is a
# way of writing n as a sum of positive integers. Two sums that differ only in the order of their
# summands are considered to be the same partition.
# The partitions of 4 are listed below:
# 1. 4
# 2. 3 + 1
# 3. 2 + 2
# 4. 2 + 1 + 1
# 5. 1 + 1 + 1 + 1
# The partitions of 8 are listed below:
# 1. 8
# 2. 7 + 1
# 3. 6 + 2
# 4. 6 + 1 + 1
# 5. 5 + 3
# 6. 5 + 2 + 1
# 7. 5 + 1 + 1 + 1
# 8. 4 + 4
# 9. 4 + 3 + 1
# 10. 4 + 2 + 2
# 11. 4 + 2 + 1 + 1
# 12. 4 + 1 + 1 + 1 + 1
# 13. 3 + 3 + 2
# 14. 3 + 3 + 1 + 1
# 15. 3 + 2 + 2 + 1
# 16. 3 + 2 + 1 + 1 + 1
# 17. 3 + 1 + 1 + 1 + 1 + 1
# 18. 2 + 2 + 2 + 2
# 19. 2 + 2 + 2 + 1 + 1
# 20. 2 + 2 + 1 + 1 + 1 + 1
# 21. 2 + 1 + 1 + 1 + 1 + 1 + 1
# 22. 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
# Create a function that receives one integer: x. If the value received is 0 or negative, or if it is
# greater than 255, the function should return -1
# The function should return the number of partitions x has.
# For example: If the function receives 4, it should return 5. If it receives 8, it will return 22, etc.
# The function will receive one integer, return another integer.
# David Alvarez C
def exercise20(number):
    aux = [ _ for _ in range(1,number)]
    cont = 1
    # def partitons(aux):
    out = []
    for i in aux:
        if i != number:
            # a este arreglo debo agrgarle un numero consecutivamente incrementalmente,
            # y probar hasta que su suma sea igual al numero
            array_aux =[i]

            while sum(array_aux) != number and sum(array_aux) < number:
                    array_aux.append(1)
            out.append(array_aux)
        
                
                # while sum(array_aux) != number and sum(array_aux) < number:
                #     array_aux = [i,i+1]
                # debe hacerse una funcion recursiva  donde el arreglo que se le pase a esa funcion 
                # este agregado un nuevo elemento incrementado en uno
    return cont

if __name__ == '__main__':
    print(exercise20(8))