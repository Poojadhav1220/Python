# SET FUNCTIONS AND METHODS

print("SET FUNCTIONS AND METHODS")
s1 = {1,2,3,12,4}
s2 = {3,4,5,20}

# length of set
print("Length of s1 is:",len(s1))

# largest element from s1
print("Max is:",max(s1))

# smallest element from s2
print("Min is:",min(s2))

# union of two set (repeated value ekdach)
print("union of two sets:",s1.union(s2))

# intersection of two set 
print("intersection of two sets:",s1.intersection(s2))

# Difference between two set 
print("Difference is:",s1.difference(s2))

# Difference between two set 
print("Difference is:",s2.difference(s1))

#adding element
s2.add(12)
print("after adding:",s2)

#discard the element
s1.discard(3)
print("After discarding:",s1)
