# Determine if a string has all unique characters
def unique_characters(s):
  #first thought, use list() to turn string into list of characters
  str_list = list(s)
  print(f"str_list {str_list}")
  #now have a list of the characters
  #loop through list, if count > 1 of current char, then not unique
  for char in str_list:
    if str_list.count(char) > 1:
      return False
  return True

print('unique_characters')
print(unique_characters('asdfgh'))
print(unique_characters('asdfah'))
print(unique_characters('asdf'))



def check_permutation(s1, s2):
  #first check if there's the same amount of characters
  if len(s1) != len(s2):
    return False
  
  #I like the list version better, preserves the amount of characters, although sets is faster i'm guessing
  #if same length, convert to lists, maybe sets?
  #sets are tailor made for this kind of operation it seems, but lemme try with sorted list
  # s1List = set(s1)
  # s2List = set(s2)
  # print(f"s1List: {s1List}")
  # print(f"s2List: {s2List}")

  # #sort lists, then check if they are equal, if so return true, otherwise not permutation
  # return s1List == s2List

  s1List = sorted(list(s1))
  s2List = sorted(list(s2))

  return s1List == s2List


print('check_permutation')
print(check_permutation('cars', 'raas'))
print(check_permutation('butt', 'btu'))
print(check_permutation('wat', 'twa'))
print(check_permutation('SETAMR', 'ZAQEWR'))

def URLify(s):
  # with python method
  new_string = s.replace(" ", "%20")
  return new_string

#   #without
#   strList = list(s)
#   for idx, char in enumerate(strList):
#     if char == " ":
#       strList[idx] = "%20"
#   return "".join(strList)

print("URLify")
print(URLify("big fluffy clouds"))

# check if string is permutation of a palindrome
def palindrome_permutation(s):
  #get rid of spaces?
  s = s.replace(' ', '')


  #edge cases
  if len(s) == 0:
    return False
  
  if len(s) == 1:
    return True

  #a palindrome can have no more than 1 character that is odd
  #therefore, need to count occurances of characters in string, if more than 1 odd count, return false
  str_list = list(s)
  char_count = {}

  #count characters
  for char in str_list:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1

  #characters counted, count number of odd characters
  odd_count = 0
  for value in char_count.values():
    if value % 2 == 1:
      odd_count += 1

  #0 or 1 odd characters returns True, more than 1 returns False
  if odd_count <= 1:
    return True
  else:
    return False

print('palindrome_permutation')
print(palindrome_permutation('tact coa'))
print(palindrome_permutation('avid divas'))

# find if two strings are one edit away
def one_away(s1, s2):
  #if equal then return true
  if s1 == s2:
    return True

  #can easily check if more than one edit away in case of removing or adding
  if len(s1) > len(s2) + 1 or len(s1) < len(s2) - 1:
    return False

  #check for number of different characters
  str_list = list(s1)
  diff_count = 0
  for char in str_list:
    if char not in s2:
      diff_count += 1
  
  return diff_count < 2

print('one_away')
print(one_away('abc', 'abc'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bake'))
print(one_away('pale', 'bae'))

def string_compression(s):
  # count characters
  # maybe build a list with the character and its count as entries, then build compressed string based on said list

  str_list = list(s)
  compressed_list = []

  repeat = 1
  for idx, char in enumerate(str_list):
    if((idx + 1) < len(str_list) and char == str_list[idx + 1]):
      repeat += 1
    else:
      compressed_list.append(char)
      compressed_list.append(repeat)
      repeat = 1

  compressed_s = ''.join(map(str, compressed_list))
  if compressed_s > s:
    return s
  else:
    return compressed_s

print('string compression')
print(string_compression('aaaaabbbbbcc'))
print(string_compression('abbccaaa'))

def rotate_matrix(matrix):

  # make sure we're dealing with a NxN matrix
  if(matrix.length == 0 or matrix.length != matrix[0].length):
    return False
  
  n = matrix.length

  for layer in range(0,n):
    if layer < n/2:  
      break
    first = layer
    last = n - 1 - layer
    for i in range(first, last):
      offset = i - first

      top = matrix[first][i]

      # left -> top
      matrix[first][i] = matrix[last-offset][first]

      # bottom -> left
      matrix[last-offset][first] = matrix[last][last-offset]

      # right -> bottom
      matrix[last][last-offset] = matrix[i][last]

      # top -> right
      matrix[i][last] = top

  return matrix


def zero_matrix(matrix):
  # setup secondary arrays to capture 0 values
  row = []
  column = []

  # store row and column index with 0 value
  for i in matrix:
    for j in column:
      if matrix[i][j] == 0:
        row[i] = True
        column[j] = True

  # nullify rows
  for i in row:
    if row[i] == True:
      nullify_row(matrix, i)

  # nullify columns
  for j in column:
    if column == True:
      nullify_column(matrix, j)

  #helper functions
  def nullify_row(matrix, row):
    for j in matrix[row]:
      matrix[row][j] = 0

  def nullify_column(matrix, col):
    for i in matrix:
      matrix[i][col] = 0

  return matrix

def string_rotation(s1, s2):
  # check that s1 and s2 are equal length and not empty
  if len(s1) == len(s2) and len(s1) > 0:
    s2s2 = s2 + s2
    if is_substring(s1, s2s2):
      return True
    else:
      return False
  else:
    return False

