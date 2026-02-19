# Comprehensive list: 
# Write a list comprehension to generate squares of numbers from 1 to 10. 


squares = [x**2 for x in range(1, 11)]
print(squares)


s3 = [x**3 for x in range(1,11)]             # This is for cube
print(s3)



#---------------------------#---------------------------#---------------------------#--------------------------------------

#2. Create a list of even numbers between 1 and 50 using list comprehension

ev =[x for x in range(1,50)
    if x % 2 != 0 ]

print(ev)

#---------------------------#---------------------------#---------------------------#--------------------------------------


#3. Convert all strings in a list to uppercase using list comprehension. 


words = ["apple", "banana", "cherry"]
upper_words = [w.upper() for w in words]

print(upper_words)



#OR

p = "pratham"
print(p.upper())







#---------------------------#---------------------------#---------------------------#--------------------------------------

#4. Given a list of integers, create a new list that contains only the positive numbers. 


nums = [-5, 3, -1, 7, 0]
positive = [x for x in nums 
            if x > 0]
print(positive)



#---------------------------#---------------------------#---------------------------#--------------------------------------


#5. Create a list of tuples (num, num^2) for numbers 1 to 5. 


p = [(x,x**2) for x in range(1,6)]
print(p)


pairs = [(x, x**2) for x in range(1, 6)]
print(pairs)



#---------------------------#---------------------------#---------------------------#--------------------------------------


#6. Extract all vowels from a given string using list comprehension. 


text = "Pratham Ghumare"

vowels = [ch for ch in text 
          if ch in"aeiouAEIOU"]

print(vowels)



#---------------------------#---------------------------#---------------------------#--------------------------------------



# 7. Flatten a 2D list using list comprehension. 

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]

print (flat)



#---------------------------#---------------------------#---------------------------#--------------------------------------


#8. Replace all negative numbers in a list with 0 using list comprehension. 


nums = [-5, 3, -1, 7, 0 , 2 , 3 ]
result = [x if x > 0 else 0 for x in nums]

print(result)



#---------------------------#---------------------------#---------------------------#--------------------------------------

#9. Given a list of words, create a list of lengths of each word. 


words = ["Python", "SQL", "Data"]
lengths = [len(w) for w in words]

print(lengths)	


#---------------------------#---------------------------#---------------------------#--------------------------------------

#10. Filter out words that start with the letter 'A' or 'a'. 

words = ['apple', 'banana', "Avocado", "grape", "apricot", "Mango"]

a = [i for i in words if i.startswith(('A','a'))]
print(a)





#---------------------------#---------------------------#---------------------------#--------------------------------------


# 11. From a list of numbers, generate a list of “even” or “odd” strings using 
# list comprehension. 
# (Like → [“even”, “odd”, “odd”, “even”…])


nums = [1, 2, 3, 4]
result = ["even" if x % 2 == 0 else "odd" for x in nums]

print(result) 


#---------------------------#---------------------------#---------------------------#--------------------------------------


#12. Create a list of numbers divisible by both 3 and 5 in range 1–100. 



num = [n for n in range(1,101) if n % 3 == 0 and n%5 == 0]

print(num)



#---------------------------#---------------------------#---------------------------#--------------------------------------

# 13. Write a nested list comprehension to generate a multiplication table 
# for 1–5. 

table = [[i * j for j in range(1, 11)] for i in range(1, 6)]

print(table)



#---------------------------#---------------------------#---------------------------#--------------------------------------



#14. Convert a dictionary’s keys into a list using list comprehension. 

d = {"a": 1, "b": 2, "c": 3}

keys_list = [key for key in d]

print(keys_list)





#---------------------------#---------------------------#---------------------------#--------------------------------------




#15. Extract numeric digits from a string using list comprehension. 


s = "abc123xyz456"
p ='dwjeh2h4j36jg757jljkbdb2jbj3b'


digits = [char for char in s if char.isdigit()]
d2 =[ch for ch in p if ch.isdigit()]

print(d2)
print(digits)





#---------------------------#---------------------------#---------------------------#--------------------------------------



#16. Use list comprehension to remove all spaces from a string. 


s = "Hello World Python"

no = "".join([char for char in s if char != " "])

print(no)





#---------------------------#---------------------------#---------------------------#--------------------------------------


#17. Create a list of characters that appear more than once in a string. 

s = "programming"

dupli= [char for char in set(s) if s.count(char) > 1]

print(dupli)





#---------------------------#---------------------------#---------------------------#--------------------------------------



# 18. From a list of sentences, generate a list of all words (split using list 
# comprehension). 

sentences = ["Hello world", "Python is powerful"]

words = [word for sentence in sentences for word in sentence.split()]

print(words)



#---------------------------#---------------------------#---------------------------#--------------------------------------



# 19. Create a list of unique elements from a list using list comprehension + 
# condition. 


nums = [1,2,2,3,4,4,5]

unique = [x for i, x in enumerate(nums) if x not in nums[:i]]

print(unique)




#---------------------------#---------------------------#---------------------------#--------------------------------------

# 20. Generate all pairs (x, y) where x is from list A and y is from list B 
# (cartesian product). 


A = [1, 2, 3]
B = ["a", "b"]


pairs = [(x, y) for x in A for y in B]

print(pairs)




#---------------------------#---------------------------#---------------------------#--------------------------------------




# Lambda functions 


# 1. Write a lambda to add two numbers. 


add = lambda a, b: a + b

print(add)





#---------------------------#---------------------------#---------------------------#--------------------------------------

# 2. Create a lambda to check if a number is even. 

even = lambda x: x % 2 == 0

print(even(4))



#---------------------------#---------------------------#---------------------------#--------------------------------------
# 3. Write a lambda to get the last character of a string. 

last_char = lambda s: s[-1]
print( last_char("Python"))



# #---------------------------#---------------------------#---------------------------#--------------------------------------
# 4. Use lambda with map() to square every number in a list. 


nums = [1, 2, 3, 4]
x = list(map(lambda x: x**2, nums))
print(x)




#---------------------------#---------------------------#---------------------------#--------------------------------------

# 5. Use lambda with filter() to get only odd numbers from a list. 


nums = [1, 2, 3, 4, 5]
p = list(filter(lambda x: x % 2 != 0, nums))
print(p)




#---------------------------#---------------------------#---------------------------#--------------------------------------
# 6. Use sorted() + lambda to sort a list of tuples by second value. 


data = [(1, 3), (4, 1), (2, 2)]
x = sorted(data, key=lambda x: x[1])
print(x)




# #---------------------------#---------------------------#---------------------------#--------------------------------------
# 7. Create a lambda to check if a string is a palindrome. 

pal = lambda s: s == s[::-1]
print(pal("madam"))




#---------------------------#---------------------------#---------------------------#--------------------------------------
# 8. Use lambda to find maximum of three numbers. 

max = lambda a, b, c: max(a, b, c)
print(max(3, 7, 5))



#---------------------------#---------------------------#---------------------------#--------------------------------------
# 9. Write a lambda to reverse a string. 

rev = lambda s: s[::-1]
print( rev("Python"))




#---------------------------#---------------------------#---------------------------#--------------------------------------
# 10. Use lambda with map() to convert a list of strings to integers. 

nums = ["1", "2", "3"]
x = list(map(lambda x: int(x), nums))

print(x)



#---------------------------#---------------------------#---------------------------#--------------------------------------

# 11. Use lambda with filter() to remove empty strings from a list. 

data = ["hi", "", "hello", ""]
x =  list(filter(lambda x: x != "", data))
print(x)





#---------------------------#---------------------------#---------------------------#--------------------------------------

# 12. Use lambda to compute factorial using reduce() (yeah, that one-liner madness). 







#---------------------------#---------------------------#---------------------------#--------------------------------------
# 13. Write a lambda that returns the larger of two numbers. 


larger = lambda a, b: a if a > b else b
print(larger(10, 20))



#---------------------------#---------------------------#---------------------------#--------------------------------------
# 14. Use lambda to check if number is divisible by 5. 


div5 = lambda x: x % 5 == 0

print(div5(25))





# #---------------------------#---------------------------#---------------------------#--------------------------------------
# 15. Use lambda + map() to add 10 to each element of a list. 

nums = [1, 2, 3]
x = list(map(lambda x: x + 10, nums))
print(x)



#---------------------------#---------------------------#---------------------------#--------------------------------------

# 16. Use lambda to sort a list of dictionaries by a key (like "age"). 


people = [{"name": "A", "age": 30}, {"name": "B", "age": 20}]
x= sorted(people, key=lambda x: x["age"])
print(x)





#---------------------------#---------------------------#---------------------------#--------------------------------------
# 17. Write a lambda that returns True if a character is a vowel. 

v = lambda c: c.lower() in "aeiou"
print(v("A"))




#---------------------------#---------------------------#---------------------------#--------------------------------------

# 18. Use lambda + filter to extract words of length > 5 from a list. 

words = ["python", "hi", "developer"]
x = list(filter(lambda x: len(x) > 5, words))
print(x)




#---------------------------#---------------------------#---------------------------#--------------------------------------


# 19. Use lambda to calculate the area of a circle (πr²). 


area = lambda r: 3.1416 * r**2
print( area(5))




#---------------------------#---------------------------#---------------------------#--------------------------------------

# 20. Write a lambda to remove duplicates from a list using filter + set.

nums = [1, 2, 2, 3, 3, 4]
x = list(set(nums))
print(x)




#---------------------------#---------------------------#---------------------------#-------------------------------------- 



# 21. Use lambda with reduce() to find the product of all numbers in a list.





#---------------------------#---------------------------#---------------------------#-------------------------------------- 


# 22. Write a lambda that returns absolute value of a number. 

abs_val = lambda x: x if x >= 0 else -x
print( abs_val(-10))


#---------------------------#---------------------------#---------------------------#--------------------------------------


# 23. Use lambda to sort a list of strings by their length. 


words = ["hi", "python", "cat"]
p = sorted(words, key=lambda x: len(x))
print(p)




#---------------------------#---------------------------#---------------------------#--------------------------------------

# 24. Use lambda to get only uppercase characters from a string. 

s = "PyThOn"
p = list(filter(lambda c: c.isupper(), s))
print(p)


#---------------------------#---------------------------#---------------------------#--------------------------------------

# 25. Write a lambda that returns the square if number is even, cube if odd.

calc = lambda x: x**2 if x % 2 == 0 else x**3

print( calc(4))   # even
print( calc(3))   # odd




# #---------------------------#---------------------------#---------------------------#-------------------------------------- 
# 26. Use lambda with map to convert Celsius to Fahrenheit. 



temps = [0, 10, 20, 30]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps))

print("Fahrenheit values:", fahrenheit)



# #---------------------------#---------------------------#---------------------------#--------------------------------------
# 27. Write a lambda to check if two strings are anagrams. 

is_anagram = lambda a, b: sorted(a.lower()) == sorted(b.lower())

print("Are anagrams:", is_anagram("listen", "silent"))




# #---------------------------#---------------------------#---------------------------#--------------------------------------
# 28. Use lambda to extract only numeric values from a mixed list. 

data = [1, "hello", 3.5, "world", 10]

numbers = list(filter(lambda x: isinstance(x, (int, float)), data))

print("Numeric values:", numbers)





# #---------------------------#---------------------------#---------------------------#--------------------------------------
# 29. Use lambda inside any() to check if any list element is negative. 


nums = [5, 3, -2, 8]

has_negative = any(map(lambda x: x < 0, nums))

print("Contains negative number:", has_negative)






# #---------------------------#---------------------------#---------------------------#--------------------------------------
# 30. Use lambda to generate a function that multiplies any number by n 


multiplier = lambda n: lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print("Double value:", double(5))
print("Triple value:", triple(5))








# #---------------------------#---------------------------#---------------------------#--------------------------------------