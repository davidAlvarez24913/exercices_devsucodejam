# Given a string which contain letters (uppercase and lowercase), numbers, and special
# characters, return the same string in all lowercase.
# For example, if the function receives:
# “Ñañito, QUÉ bien! THIS is a sample text, Lorem Ipsum, 2 Be Converted.”
# The function should return:
# “ñañito, qué bien! this is a sample text, lorem ipsum, 2 be converted.”
# The function should consider converting: All characters from A-Z, Á,É,Í,Ó,Ú and Ñ. Other
# characters will remain the same.
# Limitation:
# The conversion should be done considering the ASCII values. Obviously you CAN’T use the
# functions provided by the language (toLowercase(), lowercase(), etc.). You CAN’T have a
# huge switch statement with cases for each letter, or lots of if/else statements.
# This function will receive an string and return an string
# # David Avarez C
def exercise_7(x):

    # alphabet_lowercase =list(map(chr, range(97, 123)))
    # alphabet_uppercase = list(map(chr, range(65, 91)))
    
    vowels2 = list(map(ord, ['á', 'é', 'í', 'ó', 'ú', 'ñ']))
    vowels3 = list(map(ord, ['Á', 'É', 'Ú', 'Ó', 'Ú', 'Ñ']))

    alphabet_uppercase = list( range(65, 91))
    alphabet_uppercase += vowels3
    alphabet_lowercase = list( range(97, 123))
    alphabet_lowercase += vowels2

    alphabet = [[i, j] for i, j in zip(alphabet_uppercase, alphabet_lowercase)]
    
    if isinstance(x, str) :
        aux = [ord(_) for _ in x]
        
        for value in alphabet:
            for index, valube_b in enumerate(aux):
                if value[0] == valube_b:
                    aux[index] = value[1]

        aux = [chr(_) for _ in aux]
        print('Entrada: ',x)
        return ''.join(aux)
        # return aux
    else:
        return 'Debe ingresar una cadena de texto'
            
if __name__ == '__main__':
    print(exercise_7('Ñañito, QUÉ bien! THIS is a sample text, Lorem Ipsum, 2 Be Converted.'))



    
