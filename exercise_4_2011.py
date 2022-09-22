# 4. Remove strings? Piece of cake
# Given two strings S1 and S2. Delete from S1 all those characters which occur in S2. Return
# a clean S1 with the relevant characters deleted. Any character deletes both uppercase and
# lowercase.
# For example, given:
# S1 = “DevsuCodeJam is just great!”
# S2 = “I am here!: )”
#     The function should return: “DvsuCodJsjustgt”.
#     The function will receive 2 strings and return a string
# David Avarez C

def exercise_4(x, y):
    if isinstance(x, str) and isinstance(y, str):
        letters_a = [_ for _ in x.lower()]
        letters_b = [_ for _ in y.lower()]
        letters_repeated = list(set([
            value for value in letters_a if value in letters_b]))
        
        for i in letters_repeated:
            if i in x:
                x = x.replace(i,'')
        return  x
    else:
        return 'Los parametros ingresados no son cadenas de texto'

            
if __name__ == '__main__':
    print(exercise_4('DevsuCodeJam is just great!', 'I am here!: )'))
    print('DvsuCodJsjustgt2')



    
