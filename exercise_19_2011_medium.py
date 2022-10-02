# 19. Ok, let’s the party begin...
# Create a function that receives a 32 bit integer and return the number of ones in the binary of
# that number. (caution: looping through testing each bit is not a solution).
# The function can receive any positive 32 bit integer.
# For example:
# If the function receives 25, it should return 3. Why? Because 25 in binary is 11001, which
# has 3 ones.
# The function will receive an integer and return an integer.
# David Alvarez C

def exercise_19(int_32):
    if int_32 > 0 and int_32 < pow(2,32):
        aux_array = [_ for _ in bin(int_32)[2:] if _ =='1']
        # x = list(filter(lambda x: x == '1', bin(int_32)[2:]))
        out = len(aux_array)        
        return out
    else:
        return 'the integer is not within the domain.'
    
if __name__ == '__main__':
    print(exercise_19(10))
    print(exercise_19(4294967295))
