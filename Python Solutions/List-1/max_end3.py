"""Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""
# with a loop

def max_end3(nums):
    new = []
    def new_append(num):
        for i in range(3):
            new.append(num)
    if nums[0] > nums[-1]:
        new_append(nums[0])
    else:
        new_append(nums[-1])
    return new

# without a loop

def max_end3(nums):
    if nums[0] > nums[-1]:
        return [new[0],new[0],new[0]]
    else:
        return [nums[-1],nums[-1],nums[-1]]