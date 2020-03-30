#problem 1 Write a function called letter_count that takes a string and a single character, 
# and returns the number of times that character appears in the string.

#letter_count('abcde', 'a') #should return 1
#letter_count('this is going to be easy', 'i') #should return 3
#letter_count('how about that?', 'z') #should return 0

letter_count = "how about that?"
count = 0
  
for letter in letter_count: 
    if letter == 'z': 
        count = count + 1
  
print(count)

#Problem 2 Write a function called count_words that takes a string and returns the number of words in the string.
#count_words('hey there!!') #should return 2
#count words('I\'m staying home because of the epidemic') # shoud return 7
#count_words('how-about-a-hypenated-string?') #shoud return 1

count_words = 'I\'m staying home because of the epidemic'
count = 0

for words in count_words:
    count = len(count_words.split())

print(count)


#Problem 3 Write a function called reverse_list that takes a list and returns a new list with the items reversed.
#reverse_list([]) # should return []
#reverse_list([1, 2, 3]) # should return [3, 2, 1]
#reverse_list(['this', 'is' 'cool!']) #should return ['cool!', 'is' , 'this']

def reverse_list(my_list):
    result = []
    for char in my_list:
        result = [char] + result
    return result

print(reverse_list(['this','is', 'cool!']))


# Problem 4 write a function called split_list that takes a list of integers and an integer (called the pivot), and returns a list containing two lists:
# one with all the numbers less than the pivot
#the other with all the numbers greater than or equal to the pivot
#split_list([1, 2, 3], 0) # should return [[], [1, 2, 3]]
#split_list([4, 5, 11, 8, 19], 10) #should return [[4, 5, 8], [11, 19]]
#split_list([5, 6, 20, -4, -12, 0], -1) # should return [[-4, -12], [5, 6, 20, 0]]

#return the items that are in both lists 1 and 2 in a new list

def split_list(input_list,pivot):
    result_one = []
    result_two = []
    for item in input_list:
        if item >= pivot:
            result_two.append(item)
        else:
            result_one.append(item)

    return [result_one, result_two]

print(split_list([5, 6, 20, -4, -12, 0], -1))
'''

#Problem 5 (Optional) Write a function called is_isogram that takes a string and returns true if all the characters are unique (no
#repeated characters), or returns false otherwise.
#is_isogram('abc') #should return True
#is_isogram('hi there') #should return False
#is_isogram('Hapy coding!') #should return True

def is_isogram(''):
    if t
'''


