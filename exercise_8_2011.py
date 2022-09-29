# 8. A-Words
# Given a string, find the number of words that has at least one “a” character(uppercase or
#                                                                              lowercase).
# Do not take into account character variations like á, à, etc... only the simple “a”
# and “A” counts.
# The words are always separated by a space, a comma, a semicolon or a dot.
# For example:
# If the function receives: “this is a sample text, it has a lot of analysis.” The function should
# return 5, since five words has “a” characters. (a, sample, has, a, analysis).
# The function will receive a string and return an integer.
# Limitations: Do not use the split() function, or similar.
# David Alvarez C
import exercise_7_2011
def exercise_8(sentence, letter):
    sentence = exercise_7_2011.exercise_7(sentence)
    sentence_array =[ s for s in sentence]
    array_aux = [ index for index, value in enumerate(sentence_array) if value == ' ']
    array_aux_2 = [[value+1, array_aux[index+1]] for index, value in enumerate(
        array_aux) if index+1 < len(array_aux)]
    array_aux_3 = [sentence[:array_aux_2[0][0]-1]]
    for j in array_aux_2:
        array_aux_3.append(sentence[j[0]:j[1]])
    array_aux_3.append(sentence[array_aux_2[-1][1]:])

    count = 0 
    print(array_aux_3)
    for x in array_aux_3:
        if letter in x:
            count += 1


    return count
if __name__ == '__main__':
    print(exercise_8('this is a sample text, it has a lot of analysis.','a'))
    print(exercise_8(
        'Ñañito, QUÉ bien! THIS is a sample text, Lorem Ipsum, 2 Be Converted.','é'))
    # print( 'e' == 'é')
