"""
Given a list integers nums and an integer max, find the **number of elements** in the list that are **less than or equal to** max.

Examples
Input  : nums = [0, 5, 5, 5, 4], max = 5
Output : 5
Input  : nums = [5, 6, 7], max = 4
Output : 0 
"""

def q6(nums, maxNum):
    returnList = []
    for num in nums:
      # if num >= maxNum:
      if num <= maxNum:
         returnList.append(num)
    # return returnList
    return len(returnList)


"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

def q7(digits):
  digits[-1] = digits[-1] + 1
  return digits

"""
Given an array of integers nums and an integer target, return **indices** of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and **you may not use the same element twice**. You should return the indices in increasing order (ascending order).
"""

def q8(nums, target):
  for i in range(0, len(nums)):
    for j in range (1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]
      
# pythonic solution given for q8:
def target_sum(nums, target):
  for idx, val in enumerate(nums):
    if target - val in nums[idx + 1:]:
      return [idx, nums[idx + 1:].index(target - val) + (idx + 1)]

if __name__ == '__main__':
  #  print('hello')
  print('q6 ex 1:', q6([0, 5, 5, 5, 4], 5)) # expected: 5
  print('q6 ex 2:', q6([5, 6, 7], 4)) # expected: 0
  print('q7 ex:', q7([1,0,2])) # expected: [1,0,3]
  print('q8 ex 1:', q8([1,2,4,3,6,5,7], 10)) # expected: [2,4]
  print('q8 ex 2:', q8([2,3,8,4], 7)) # expected: [1,3]
