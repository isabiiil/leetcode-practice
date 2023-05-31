"""
Write a function standard_to_military() that takes three parameters hours, mins, and time_of_day that returns the hours and minutes converted from 12-hour format to 24-hour format.

Notes:
Midnight is 12:00 AM on a 12-hour clock and 00:00 on a 24-hour clock
Noon is 12:00 PM on 12-hour clock and 12:00 on 24-hour clock
"""

def standard_to_military(hours, mins, time_of_day):
  military = ""
  if time_of_day == "PM":
    hours += 12
  military = str(hours) + ":" + str(mins)
  if mins == 0:
    military += "0"
  return military

"""
A palindrome is a sequence that reads the same backward as forward. Write a function is_palindrome() that takes an integer list num_list as a parameter and outputs either True or False if it is a palindrome.
"""

def is_palindrome(num_list):
  # for i in range(len(num_list)//2):
  #   for j in range(len(num_list)-1, len(num_list)//2, -1):
  #     if num_list[i] != num_list[j]:
  #       return False
  # return True
  for i in range(len(num_list)//2):
    if num_list[i] != num_list[len(num_list)-i-1]:
      return False
  return True

"""
Write a function rotate_right() that takes an integer list num_list and returns the list with its elements rotated to the right. A list is said to be right rotated if all elements of the array are moved to its right by one position.
"""

def rotate_right(num_list):
  temp = num_list[-1]                       # save the last element
  for i in range(len(num_list)-1, 0, -1):   # starting from the back, 
    num_list[i] = num_list[i-1]             # copy that element's left element
  num_list[0] = temp                        # then return the last element to the right 
  return num_list

"""
Write a function that rotate_elements() that takes an integer list num_list and an integer k. The function should return num_list with its elements rotated to the right k number of times.
"""

def rotate_elements(num_list, k):
  temp = num_list[len(num_list)-k:]   # copy all the last elements that would end up in the front of the new array
  for i in range(k):
    num_list.pop()                    # get rid of those elements in the original array
  temp.reverse()                      # put those last elements in reverse order for proper insertion in next step
  for x in temp:
    num_list.insert(0, x)             # insert all rotated elements in the right order
  return num_list

# helper function separated in given solution
def rightRotateByOne(num_list):
  last = num_list[-1]
  for i in reversed(range(len(num_list) - 1)):
    num_list[i + 1] = num_list[i]
  num_list[0] = last
 

def rotate_elements(num_list, k):
  if k < 0 or k >= len(num_list):
    return
  for i in range(k):
    rightRotateByOne(num_list)


if __name__ == '__main__':
  # print('hello')
  print('q6 ex1:', standard_to_military(4,40,'PM')) # expected 16:40
  print('q6 ex2:', standard_to_military(8,00,'AM')) # expected 8:00
  print('q7 ex1:', is_palindrome([1,2,3,4,5])) # expected False
  print('q7 ex2:', is_palindrome([1,2,3,2,1])) # expected True
  print('q7 ex3:', is_palindrome([3,4,4,3])) # expected True
  print('q7 ex4:', is_palindrome([3,6,4,3])) # expected False
  print('q8 ex1:', rotate_right([1,2,3,4])) # expected [4,1,2,3]
  print('q8 ex2:', rotate_right([4,3,2,6,1])) # expected [1,4,3,2,6]
  print('q8 ex3:', rotate_right([5,6,3,2,2,1])) # expected [1,5,6,3,2,2]
  print('q11 ex1:', rotate_elements([1,2,3,4,5,6,7], 3)) # expected [5,6,7,1,2,3,4]
  print('q11 ex2:', rotate_elements([1,2,3,4,5,6,7], 6)) # expected [2,3,4,5,6,7,1]
  print('q11 ex3:', rotate_elements([1,2,3,4,5,6,7], 2)) # expected [6,7,1,2,3,4,5]
  print('q11 ex4:', rotate_elements([1,2,3,4,5,6,7], 7)) # expected [1,2,3,4,5,6,7]
  