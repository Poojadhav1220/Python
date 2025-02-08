# STRING FUNCTIONS AND METHODS

print("STRING FUNCTIONS AND METHODS")
a = "My name is Pooja"

# length of a string
print("length:",len(a))

# converts all characters to lowercase
print("Lowercase:",a.lower())

# converts all characters to uppercase
print("Uppercase:",a.upper())

# capitalize the first letter
print("Capitalized:",a.capitalize())

#replace the word
print("Replaced 'Pooja' with 'Aadu':",a.replace("Pooja","Aadu"))

# splits a string into list
print("Splitted string into list:",a.split())

# find the index
print("index of 'pooja':",a.find("Pooja"))

#return true if all charcters are alphabetic otherwise false
print("are characters alphabetic? :",a.isalpha())

#check starting with specified value
print("checked starting with 'pooja'?:",a.startswith("Pooja"))


# for line with dashes
print("\n  "+"-"*50+"  \n")