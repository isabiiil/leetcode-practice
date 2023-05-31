"""
Given a list of words followed by two words, find the distance between the two words
"""

def q7(wordList, word1, word2):
  for i in range(len(wordList)):
    for j in range(1, len(wordList)):
      if (wordList[i] == word1 and wordList[j] == word2) or (wordList[j] == word1 and wordList[i] == word2):
        return i-j if i>j else j-i
  return -1

"""
Write a function military_to_standard() that takes two integer as parameters hours and mins, that returns the time converted from 24-hour format to 12-hour format.

Notes:
Midnight is 12:00 AM on a 12-hour clock and 00:00 on a 24-hour clock
Noon is 12:00 PM on 12-hour clock and 12:00 on 24-hour clock
"""
def military_to_standard(hours, mins):
  time = str(hours % 12) + ":" + str(mins)
  if hours < 13:
    time += "AM"
  else:
    time += "PM"
  return time

"""
Given an integer n, convert the function to the corresponding roman numbers
"""

def roman(n):
  roman = ""
  while n > 0:
    if n >= 100:
      roman += "C"
      n -= 100
    if n >= 90:
      roman += "XC"
      n -= 90
    if n >= 50:
      roman += "L"
      n -= 50
    if n >= 40:
      roman += "XL"
      n -= 40
    if n >= 10:
      roman += "X"
      n -= 10
    elif n == 9:
      roman += "IX"
      n -= 9
    elif n == 8:
      roman += "VIII"
      n -= 8
    elif n == 7:
      roman += "VII"
      n -= 7
    elif n == 6:
      roman += "VI"
      n -= 6
    elif n == 5:
      roman += "V"
      n -= 5
    elif n == 4:
      roman += "IV"
      n -= 4
    elif n == 3:
      roman += "III"
      n -= 3
    elif n == 2:
      roman += "II"
      n -= 2
    elif n == 1:
      roman += "I"
      n -= 1
  return roman

# non brute force solution for q9:
def to_roman(num):
  res = ""
  table = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
  ]
  for cap, roman in table:
    d, m = divmod(num, cap)
    res += roman * d
    num = m

  return res

      
if __name__ == '__main__':
  #  print('hello')
  print('q7 ex1:', q7(['yes', 'no', 'maybe', 'hi'], 'yes', 'hi')) # expected 3
  print('q7 ex2:', q7(['yes', 'no', 'maybe', 'hi'], 'yes', 'maybe')) # expected 2
  print('q7 ex3:', q7(['yes', 'no', 'maybe', 'hi'], 'maybe', 'yes')) # expected 2
  print('q8 ex1:', military_to_standard(18, 12)) # expected 6:12PM
  print('q8 ex2:', military_to_standard(4, 20)) # expected 4:20AM
  print('roman test 12', roman(12))
  print('roman test 19', roman(19))
  print('roman test 99', roman(99))

  print('q9 ex1:', roman(24)) # expected XXIV
  print('q9 ex2:', roman(67)) # expected LXVII
  print('q9 ex3:', roman(12)) # expected XII
  print('q9 ex4:', roman(149)) # expected CXLIX
  print('q9 ex5:', roman(151)) # expected CLI
  # print('q9 ex6:', roman(395)) # expected CCCXCV
  # 999
