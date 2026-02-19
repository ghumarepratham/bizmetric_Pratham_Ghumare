# 1.	If  name = ''' Hi How are you? Starterd learning python. It's really interesting.''' 
# Then what is the output of following code



# •	name[:] 
# •	name[-10:-5]
# •	name[3:12]
# •	name[12:3]
# •	name[5,6]
# •	name[-4:-12]
# •	name[::2]
# •	name[::-2]

#output:
# name = '''Hi How are you? Starterd learning python. It's really interesting.'''
# print(name[:] ) #output the entire string
# print(name[-10:-5]) #output from 10th last to 5th last character =  'teres'
# print(name[3:12]) #output from index 3 to index 12 = ' How are y'
# print(name[12:3]) #output will be empty string as starting index is greater than ending index
# print(name[5:6]) #output character at index 5 = 'w'
# print(name[-4:-12])#output will be empty string as starting index is greater than ending index
# print(name[::2]) #output every 2nd character in the string
# print(name[::-2]) #output every 2nd character in reverse order


# #----------------------------------------------------------------


# 2.	 L1 = [‘a’ , ‘b’, 20, 30, ‘t’, 100, 300, 400, ‘Happy’, ‘major’]
# a.	L1[:]
# b.	L1[::3]
# c.	L1[::-2]
# d.	How to extract  value “Happy” based on index and negative index
# e.	How to check type of data in list at 4th position
# f.	Extract values for 100, 300, 400 

# #output:
# L1 = ['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
# print(L1[:]) #output the entire list
# print(L1[::3]) #output every 3rd element in the list
# print(L1[::-2]) #output every 2nd element in reverse order

# print(L1.index('Happy'))
# print(L1[8]) #`output 'Happy' using index
# print(L1[-3]) #output 'Happy' using negative index

# print(type(L1[4])) #output the type of data at 4th position
      
# print(L1[5:8]) #output values for 100, 300, 400

      

# #----------------------------------------------------------------



# 3.	If l2 =[1,2,3,5,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”] then what is the output of following
# •	L2[4]
# •	L2[1:5]
# •	L2[7]
# •	L2[7][2]
# •	L7[7][2:]
# •	L2[ : 3]
# •	L2[3:]

# l2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, "Success"]
# print(l2[4]) # Output is 4th index value
# print(l2[1:5]) #output from 1th index till 4th
# print(l2[7])   #output should be 7th Index : 'Success'
# print(l2[7][2]) #output will be 7th indexs string 2th index Character : c
# print(l2[7][2:]) #output will be 7th index string from 2th index Character to last  : ccess
# print(l2[: 3])  # output from starting to 2nd of index : "[1, 2, 3]"
# print(l2[3: ])  #output from 3index till last : "[5, ['a', 'b', 'work hard'], 100, 200, 'Success']"


# #----------------------------------------------------------------

# # 4.	From the above l2 value ‘b’ must be changed to ‘BEE’.

# l2[4][1] = 'BEE'
# print(l2)

# #----------------------------------------------------------------

# # 5.	From l2 “BEE” has to discard.

# print(l2)
# l2[4].remove('BEE')
# print(l2[4][1])
# print(l2)

# #----------------------------------------------------------------



# # 6.	In l2 add a dictionary at the end {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}

# d =  [{'insect': ['bee', 'moth'] , 'bird' : ['parrot', 'sparrow']}]

# l2.extend(d)
# print(l2)



# #----------------------------------------------------------------



# # 7.	From l2 extract insect information.

# insect_in = l2[-1]['insect']
# print(insect_in)

# bird_info = l2[-1]['bird']
# print(bird_info)


# #----------------------------------------------------------------

# # 8.	Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of l2

# d1 = {'a':10, 'b':20, 'c' : 30}

# l2.insert(2, d1)
# print(l2)

# #----------------------------------------------------------------

# # 9.	Based on new l2 created here extract the value 10 from l2 dictionary.

# print(l2)
# print(l2[2]['a'])


# #----------------------------------------------------------------


# 10.	If l2 =[1,2,3,5, (90,40,50,10), ‘Python’, 400 ,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”, 
# (200,300, “Hundreds”)] then what is the output of following



# •	L2[4][2]
# •	L2[5][:]
# •	L2[2] [:]
# •	L2[1:5]
# •	L2[5]
# •	L2[5][3:-1]
# •	L2[-1]
# •	L2[-4, -3]
# •	L2[-4: -10]
# •	L2[7][2]
# •	L7[-7][[2:]
# •	L2[ :- 3]
# •	L2[-3:]

# l2 =[1,2,3,5, (90,40,50,10), 'Python', 400 ,['a', 'b', 'work hard'],100 , 200, 'Success',(200,300, 'Hundreds')]

# print(l2[4][2])   # output will 4th index 2nd character
# print(l2[5][:])   #5th index full string
# #print(l2[2] [:]) #syntax error
# print(l2[1:5])    # output will be 1index till 4th index
# print(l2[5])      # Output will be 5 the index : Python
# print(l2[5][3: -1]) #output will be 5 index 3rd to n-1 means : 'ho'
# print(l2[-1])      #last index means -1 :  (200,300, 'Hundreds')
# #print(l2[-4,-3])   # error
# print(l2[-4: -10])   
# print(l2[7][2])  # output is 7th index in tha 2nd index character
# print(l2[-7][2:])  #output will -7th index from last in that from 2nd charcter index till last : thon
# print(l2[: -3])  #output from starting index till -3 index 
# print(l2[-3 : ]) #output from -3 index till last index






#------------------- IF-elif-else:


# 11.	Ask user to enter the marks and define if the user got distinction, first class, second class,
# pass, Fails
# If marks are more than 80 output must be “You got distinction”
# For marks more than 60 output must be “You got First class”
# Marks more than 40 will display “You got second class”
# Marks more than or equal to 35 “PASS” Otherwise Fail

# marks  = input('Inpute your marks: ')

# if marks.isdigit():
#     marks = int(marks)
#     if marks < 0 or marks > 100:
#         print('Please enter valid marks')
#     elif marks >= 80:
#         print('You have get Distinction')
#     elif marks > 60:
#         print('You got First Class')
#     elif marks > 40:
#         print('You got Second Class')
#     elif marks >= 35:
#         print('You are PASS') 
#     else:
#         print('You are FAIL')
                           


# #----------------------------------------------------------------


# 12. Ask user to enter information about salary of the employee per year and rating received as A, B, C, D
# If salary upto 5 lpa then increament based on ratings are  A = 16% , B=12%, C= 10%, D=6%
# If salary upto 10 lpa then increament based on ratings are  A = 14% , B=10%, C= 8%, D=6%
# If salary upto 15 lpa then increament based on ratings are  A = 8% , B=6%, C= 4%, D = no increment
# If salary upto 23 lpa then increament based on ratings are  A = 7% , B=5%, C= 4%, D=no

# salary = input('Enter your salary per annum in LPA: ')
# rating = input('Enter your rating (A, B, C, D): ').upper()
# if salary.replace('.','',1).isdigit():
#     salary = float(salary)
#     increment = 0
#     if salary <= 5:
#         if rating == 'A':
#             increment = 0.16
#         elif rating == 'B':
#             increment = 0.12
#         elif rating == 'C':
#             increment = 0.10
#         elif rating == 'D':
#             increment = 0.06
#     elif salary <= 10:
#         if rating == 'A':
#             increment = 0.14
#         elif rating == 'B':
#             increment = 0.10
#         elif rating == 'C':
#             increment = 0.08
#         elif rating == 'D':
#             increment = 0.06
#     elif salary <= 15:
#         if rating == 'A':
#             increment = 0.08
#         elif rating == 'B':
#             increment = 0.06
#         elif rating == 'C':
#             increment = 0.04
#         elif rating == 'D':
#             increment = 0.00
#     elif salary <= 23:
#         if rating == 'A':
#             increment = 0.07
#         elif rating == 'B':
#             increment = 0.05
#         elif rating == 'C':
#             increment = 0.04
#         elif rating == 'D':
#             increment = 0.00

#     new_salary = salary + (salary * increment)

#     print(f'Your new salary after increment is: {new_salary} LPA')
#     #print('Your new salary after increment is: LPA: ',new_salary)
#     print('Incremental salary details: ', new_salary - salary)





#------------------------------------------------


# 13.	Ask user to opt for courses for master degree based on the following
# L1 = [“HR”, “Finance”, “Marketing”, “DS”]
# Based on above subject there are two different streams. For example- HR is having HR core and HR analytics
#  and Marketing is having core and Marketing analytics. Analytics is the optional subject and having added 
# extra fees. DS is not having analytics.
# If fees for L1 is 2 lakhs for each course core subject having the same fees but analytics subject having 10% extra on 2 lakhs.
# If student opts for hostel then 2 lakhs per year is added. For food monthly 2000 .
# Transportation charges 13000 per semester. Calculate the total annual cost based on selected service.  
# User will enter values as subject, analytics(Y/N), Hostel (Y/N), food(How many months?), Transportation(semester/annual)



# #Method-1-if else
# core_fee=200000
# analytics_extra_percent=0.10
# Hostel_fee=200000
# food_per_month=2000
# transportation_per_semester=13000
# l1=['HR','Finance','Marketing','DS']
# subject=input("Which course you want to pursue(HR,Finance,Marketing,DS)").upper()
# if subject not in  l1:
#   print("Course is not available:")
# else:
#   analytics=input("Do you want analytics?(Y/N) :").upper()
#   hostel=input("Do you want hostel?(Y/N) :").upper()
#   food_months=int(input("Enter no. of foods months:"))
#   transport=input("Do you want transportation facility?(semester/Annual) :").upper()
#   course_fee=core_fee
#   if subject !="DS" and analytics=='Y':
#     analytics_fee=core_fee*analytics_extra_percent
#     course_fee+=analytics_fee
#   else:
#     analytics_fee=0
#   if hostel=='Y':
#     Hostel_fee=Hostel_fee 
#   else:
#     Hostel_fee=0
#   food_fee=food_per_month*food_months
#   if transport=='SEMESTER':
#     transport_fee=transportation_per_semester
#   elif transport=='ANNUAl':
#     transport_fee=transportation_per_semester*2
#   else:
#     print("Invalid transportation option")
#     transport_fee=0
#   total_cost=course_fee+Hostel_fee+food_fee+transport_fee 
#   print("course_fee: ",course_fee)
#   print("Hostel_Fee: ",Hostel_fee)
#   print("food_fee: ",food_fee)
#   print("Transport_Fee: ",transport_fee)
#   print("-"*50)
#   print("Total Annual Cost:",total_cost)










#-------------Practice Day 2---------------------







# # 17.	Create a=100 
# # •	Convert a to string 
# a = 100
# a_str = str(a)
# print(a_str,type(a_str))

# # •	Convert a to list   
# a_lst = [a]
# print(a_lst,type(a_lst))


# # •	Convert a to tuple  
# a_tpl = (a,)
# print(a_tpl,type(a_tpl))

# # •	Convert a to dict 

# a_dict = {'val': a}
# print(a_dict,type(a_dict))

# # •	Convert a to set 
# a_set = {a}
# print(a_set, type(a_set))


# # •	Convert to float 
# a_flt = float(a)
# print(a_flt, type(a_flt))

# Observe the errors and note it down for all conversions. 


# 8.	Create city = “Pune” 
# •	Convert to int     
# •	Convert float 
# •	Convert list  
# •	Convert tuple 
# •	Convert dict 
# •	Convert set 





# •	Obsert errors and note it down for all conversions 
# 9.	Create a list as  marks = [20,18,15,17,18] 


# # •	Convert to int 
# marks_int = int(marks)  # This will raise an error
# print(marks_int, type(marks_int))



# # •	Convert float 
# marks_flt = float(marks)
# print(marks_flt)

# # •	Convert list 
# marks_list = list(marks)
# print(marks_list)


# # •	Convert tuple 
# marks_tpl = tuple(marks)
# print(marks_tpl)


# # •	Convert dict 
# marks_dict  = {i: marks[i] for i in range(len(marks))}
# print(marks_dict)



# # •	Convert set 
# makrs_set = set(marks)
# print(makrs_set)

# #----------------------------------------------------------------

# •	observe : errors and note it down for all conversions 
# List operations 
# 10.	Create the empty list snames 
# •	 Add value 20 in the list using append 
# •	 Add value 30 in the list using extend 
# •	Add values in the list using append 
# •	Add value “WORK" in the list using extend 
# •	 Create a new list combo having the values [1, ‘a’, ‘b’ ,2 , 3] 
# •	Add sname to combo using addition operator 
# •	Add combo to snames using append 
# •	Add combo to snames using extend. 


# #----------------------------------------------------------------

# 11.	Create one list l1 having two elements and l3 having 7 elements. Now at 4th position add l1 

# l1 = ['a', 'b']
# l2 = [1,2,3,4,5,6,7]

# l2.insert(3, l1)  #adding l1 at 4th position
# print(l2)

# #----------------------------------------------------------------


# 12.	Collection is the list having values [1,2,3,[‘a’, ‘b’, ‘c’], 100, ‘Nisha’, 20.50, 90.10 ] 
# if the data is in integer or float then multiply with 5.  

# from torch import inner


# collection = [1,2,3,['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10 ]
# for i in collection:
#     if type(i) == int or type(i) == float:
#         print(i * 5) 



# # •	From the collection delete the record for “Nisha” 
# print(collection)
# collection.remove('Nisha')
# print(collection)


# # •	Find the location of 20.50 
# print(collection)
# a_index = collection.index(20.50)
# print(a_index)



# #----------------------------------------------------------------



# # 13.	Create a comprehensive list for square upto 10 

# square = [i**2 for i in range(11)]
# print(square)

# #----------------------------------------------------------------

# # 14.	Create the comprehensive list to find number divisible by 13 till 200

# lst1 = [i for i in range(200) if i%13 == 0]
# print(lst1)

# #----------------------------------------------------------------


# # 15.	Create the list which is divisible by 4 from 300 to 400  

# s1 = [i for i in range(300, 400) if i%4== 0]
# print(s1)


# #----------------------------------------------------------------

# # 16.	Create a comprehensive list to generate list up to x, y as a number. 
# # For example if x = 3 list will be x_list = [0,1,2] and y=2 then y_list =[0,1]

# # Ask user to enter values for x and y

# x = int(input('ENter the value of X: '))
# y = int(input('Enter the value of y: '))

# x_list = [i for i in range(x)]
# y_list = [j for j in range(y)]

# print(x_list)
# print(y_list)



# # Then generate a new list based on all combination of x and y.
# # For example: if x = 1 and y =2  then x_list = [0] and y_list = [0,1]
# # And output will be [[0,0],[0,1]]
# # If x=2 and y = 2 then output will be [[0,0],[0,1][1,0],[1,1]]

# u1 = [[i, j] for i in x_list for j in y_list]
# print(u1)

# #----------------------------------------------------------------



# 17.	 What is the difference between add and update methods in set?
# answer:
# The add() method in a set is used to add a single element to the set.
# The update() method is used to add multiple elements to the set from an iterable (like a list, tuple, or another set).


# #----------------------------------------------------------------


# 18.	What is the difference between append and extend methods in list? 
# answer:
# The append() method adds a single element to the end of the list.
# The extend() method adds multiple elements to the end of the list from an iterable (like a list, tuple, or set).


# #----------------------------------------------------------------

# 19.	What is the difference between pop and remove methods? 
# answer:
# The pop() method removes and returns an element at a specified index (default is the last element) from the list.
# The remove() method removes the first occurrence of a specified value from the list.

# #----------------------------------------------------------------



# 20.	What is the difference between discard, pop, remove methods? 
# answer:
# The discard() method removes a specified element from a set if it is present. If the element is not found, it does nothing and does not raise an error.
# The pop() method removes and returns an arbitrary element from a set. If the set is empty, it raises a KeyError.
# The remove() method removes a specified element from a set. If the element is not found, it raises a KeyError.

# #----------------------------------------------------------------


# 21.	How to create empty set? 
# empty_set = set()
# print(empty_set, type(empty_set))

# #----------------------------------------------------------------

# # 22.	Create the set s1 and s2 and perform set operations like union, intersection, difference, set difference.

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}


# # # Union
# print(s1 | s2)
# print(s1.union(s2))

# # # Intersection
# print(s1 & s2)
# print(s1.intersection(s2))

# # # Difference
# print(s1 - s2)
# print(s1.difference(s2))


# # # Symmetric Difference
# print(s1 ^ s2)
# print(s1.symmetric_difference(s2))


# #----------------------------------------------------------------

# 26.	Create the format mentioned here.
# *
# * *
# * * *
# * * * *



# for i in range(1,5):            #explaination: outer loop controls the number of rows, 
#     for j in range(i):           #inner loop prints '*' i times in each row.
#         print('*', end=' ')
#     print()                   
                               
    

# #----------------------------------------------------------------



# 27.	Create the format as mentioned below:
# *****
# ****
# ***
# **
# *


# for i in range(5,0,-1):          #explaination: outer loop controls the number of rows,
#     for j in range(i):           #inner loop prints '*' i times in each row.
#         print('*', end=' ')
#     print()


# #----------------------------------------------------------------


# 28.	Str_val = “ABCD” then create the format as mentioned below:
# A
# A B
# A B C
# A B C D

# st = "ABCD"
# for i in range (len(st)):     #outer loop controls the number of rows
#     for j in range(i+1):      #inner loop prints characters from index 0 to i
#         print(st[j], end=' ')
#     print()


# #----------------------------------------------------------------



# 29.	Create the format mentioned below:
# A
# BB
# CCC
# DDDD

# for i in range(1,5):            #outer loop controls the number of rows
#     for j in range(i):
#         print(chr(64+i), end='')      #inner loop prints the character corresponding to the row number
#     print()    


# #----------------------------------------------------------------


# 30.	Create the format mentioned below:
# 1
# 22
# 333
# 4444

# for i in range(1,5):
#     for j in range(i):
#         print(i, end='')
#     print()    



# #----------------------------------------------------------------


# 31.	Val = “ABCD”  based on the Val, create the format mentioned below
# D
# DC
# DCB
# DCBA


# val="ABCD"
# for x in range(1,len(val)+1):
#     print(val[::-1][:x])

    
# #----------------------------------------------------------------





# 32.	Ask user to enter the string. If string is UPGRAD then output must be
# D
# DA
# DAR
# DARG
# DARGP
# DARGPU


# s = input("Enter string: ")

# rev = s[::-1]
# for i in range(1, len(rev)+1):
#     print(rev[:i])


# #----------------------------------------------------------------



#33.	Create a list of odd numbers from 1 to 10
#1.	Using for loop
#2.	Using comprehensive list
# odd_list=[]
# for i in range(1,11):
#     if i%2!=0:
#         odd_list.append(i)
# odd_list

# #OR

# #2.	Using comprehensive list
# odd_list=[i for i in range(1,11) if i%2!=0]
# odd_list


# #----------------------------------------------------------------



##34.Create even number list using for loop from 200 to 250

# even_list=[]
# for i in range(200,250):
#     if i%2==0:
#         even_list.append(i)
# even_list


# #----------------------------------------------------------------


#35.	List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
#Multiply each and every element by 2 and display the answer


# list2 = [2, 70, 'work', 'para', 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3, 10, 302.5]
# result = []
# for item in list2:
#     result.append(item*2)
# print(result)



# #----------------------------------------------------------------



#38.Create a function to validate user first name/last name. 
#User first name/last name should contain only characters. No special characters, numbers, space in name


# Fname=input("Enter First Name: ")
# Lname=input("Enter Last Name: ")
# def validate_name():
#     if(Fname.isalpha() and Lname.isalpha() or not Fname.isdigit() and  Lname.isdigit()):
#         return Fname+" "+Lname
# Full_name=validate_name()
# Full_name


# #----------------------------------------------------------------




