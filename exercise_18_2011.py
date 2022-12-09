# 18. Sorting, the geeks way, ...
# Create a function that sorts an array of words in alphabetical order. The text will always be
# lowercase, and won’t contain any special character or number. Do not use sorting functions
# provided by the language(read the limitations).
# For example:
# If the function receives:
# A = [‘test’, ‘contest’, ‘programming’, ‘more’]
# The function should return:
# [‘contest’, ‘more’, ‘programming’, ‘test’]
# Limitations: We want to make it interesting. Do not use any sorting function(sort,
#Array.sort(), etc.) provided by the language. You can create your own sorting function.
# The function will receive an array of strings and return an array of strings
# David Alvarez C

                
def exercise18(my_array):
    aux = []
    for word in my_array:
        aux.append([ord(word[0]), word])
    salida =[]
    while len(aux) != 0 :
        minimo = min(aux)
        print(minimo)   
        salida.append(minimo)
        aux.remove(minimo)
    
        
    return list(map( lambda  q: q[1],salida))

#  considerar la suman de la conversion a su equivalente en ascii  y orderanarlos

if __name__ == '__main__':
    print(exercise18(['test', 'contest', 'programming', 'more', 'test', 'terraza', 'camara','tz','ta','a']))
