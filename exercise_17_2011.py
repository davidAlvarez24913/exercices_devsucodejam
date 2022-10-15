# 17. Words to numbers
# Create a function that transform a string into a number. The number can be between 0 and
# 255.
# For example:
# If the function receives “zero”, it should return 0.
# If the function receives “One”, it should return 1.
# If the function receives “eleven”, it should return 11.
# If the function receives “thirteen”, it should return 13.
# If the function receives “fifty five”, it should return 55.
# If the function receives “ONE HUNDRED”, it should return 100.
# If the function receives “Two hundred thirty one”, it should return 231.
# If the function doesn’t understand the string, it should return -1
# The function will receive a string and return an integer.
# David Álvarez C
from traceback import print_tb


def exercise17(number):
    if number < 0 or number >255:
        return -1
    else:
        def unidades(number):
            if number == 0:
                return 'zero'
            if number == 1:
                return 'one'
            if number == 2:
                return 'two'
            if number == 3:
                return 'three'
            if number == 4:
                return 'four'
            if number == 5:
                return 'five'
            if number == 6:
                return 'six'
            if number == 7:
                return 'seven'
            if number == 8:
                return 'eigth'
            if number == 9:
                return 'nine'
            if number == 10:
                return 'ten'
        
        if number == 11:
            return 'eleven'
        if number == 12:
            return 'twelve'
        if number == 13:
            return 'thirteen'
        if number == 14:
            return 'fourteen'
        if number == 15:
            return 'fiveteen'
        if number == 16:
            return 'sixteen'
        if number == 17:
            return 'seventeen'
        if number == 18:
            return 'eighteen'
        if number == 19:
            return 'nighteen'
        
        def decenas(number):
            if number == 20:
                return 'twenty'
            if number == 30:
                return 'thirty'
            if number == 40:
                return 'fourty'
            if number == 50:
                return 'fifty'
            if number == 60:
                return 'sixty'
            if number == 70:
                return 'seventy'
            if number == 80:
                return 'eighty'
            if number == 90:
                return 'nighty'
        if number >0  and number <= 9:
            return unidades(number)
        
        if number>= 20 and number <100:
            aux = [x for x in str(number)]
            aux_2 =int(aux[0])*10
            salida = str(decenas(aux_2)) + ' ' +str(unidades(int(aux[-1])))
            return salida
        
        if number >= 100:
            aux_3 = [x for x in str(number)]
            aux_4 = int(aux_3[1])*10
            salida = str(unidades(int(aux_3[0]))) +' hundred ' +str(decenas(aux_4)) + ' ' + str(unidades(int(aux_3[-1])))
            return salida
            
        
if __name__ == '__main__':
    print(exercise17(21))
    print(exercise17(7))
    print(exercise17(54))
    print(exercise17(79))
    print(exercise17(123))
