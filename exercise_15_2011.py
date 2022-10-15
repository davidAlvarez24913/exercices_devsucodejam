# 15. Contiguous subarrays
# Given an array of integers(positive and negative), find the contiguous subarray with the
# largest sum. Return the sum.
# The subarray can be of any length, even it could be the whole array. It could be also a single
# element.
# For example:
# If the function receives the following array:
# A = [4, -3, 7, 2, 4, -5, 1, 2]
# Some contiguous subarrays are:
# Subarray from index 0 to 1: [4, -3] sums 1
# Subarray from index 2 to 4: [7, 2, 4] sums 13
# Subarray from index 0 to 7: [4, -3, 7, 2, 4, -5, 1, 2] sums 12
# Subarray from index 0 to 0: [4] sums 4
# ….
# [4, 7, 2, 4] is NOT a contiguous subarray.
# The function will find that the contiguous subarray with the largest sum is [4, -3, 7, 2, 4],
# which sums 14. The function should return 14.
# David ALvarez C
def exercise_15(my_array):
    result =[]
    for x in range(1,len(my_array)):
        out = sum(my_array[x:])
        out2 = sum(my_array[:-x])
        result.append([out, my_array[x:]])
        result.append([out2, my_array[:-x]])

    return max(result)[1]

if __name__ == '__main__':
    print(exercise_15([4, -3, 7, 2, 4, -5, 1, 2]))
    print(exercise_15([4, -3, -7, -2, -4, -5, 1, 2]))
    print(exercise_15([4, -3, 7, 1, 12]))
    
