# 21. Spirals!

# Given a  2-D matrix of characters, write a function that returns a string with the characters

# The matrix can have any length, but it will always be a square.

# For example: Given this matrix:

# a b c
# d e f
# g h i

# Return a string with the value: “abcfihgde”
# David Alvarez C

def exercise_21(matrix):
    out =''
    if len(matrix[0]) == len(matrix):
        for i in matrix:
            out += ''.join(i)
        return out
    else:
        return 'Matrix would be square'
        

if __name__ == '__main__':
    
    print(exercise_21([['a','b','c'],['d','e','f'],['g','h','i']]))