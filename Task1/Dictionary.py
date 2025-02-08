# DICTIONARY FUNCTIONS AND METHODS

print("DICTIONARY FUNCTIONS AND METHODS")
d = {"Pooja":"Mumbai", "Aditya":"Satara", "Sayali":"Pune", "Prachi":"Malvan"}

# length of dictionary
print("Length of dictionary is:",len(d))

# largest element alphabetically
print("Max is:",max(d))

# smallest element
print("Min is:",min(d))

# get value by key
print("the address of aditya is:",d.get("Aditya"))

# update dictionary (value change)
d.update({"Prachi":"Katta"})
print("Updated dictionary is:",d)

# update dictionary (key not update but add new one)
d.update({"Diksha":"Malvan"})
print("Updated dictionary is:",d)

# remove key-value pair
d.pop("Diksha")
print("After removing:",d)

# get all keys
print("Keys?:",d.keys())

# get all values
print("Values?:",d.values())

# get all key value pairs
print("Key-value pairs:",d.items())
