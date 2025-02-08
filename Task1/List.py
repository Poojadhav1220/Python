# LIST FUNCTIONS AND METHODS

print("LIST FUNCTIONS AND METHODS")
my_lst = [1,2,3,4,5,6]

# length of a list
print("Length of a list is:",len(my_lst))

#Largest element from list
print("Largest element is:",max(my_lst))

# Smallest element from list
print("Smallest element is:",min(my_lst))

# sum of all elements
print("Sum of all elements:",sum(my_lst))

#Adds a new element at last index of list
my_lst.append('hello')
print("after appending:",my_lst)

my_lst.append(20)
print("after appending:",my_lst)


#Insert a new element in specified index
my_lst.insert(3,20)
print("After inserting:",my_lst)

#Removes the specific element
my_lst.remove(6)
print("Ater remove:",my_lst)

#pop the last element
my_lst.pop()
print("Ater pop:",my_lst)

# reversing the list
my_lst.reverse()
print("After reverse:",my_lst)

# sorting the elements (its not applicable when str and int in it)
'''my_lst.sort()
print("After sorting:",my_lst)'''

my_lst.remove('hello')
my_lst.sort()
print("After sorting:",my_lst)

