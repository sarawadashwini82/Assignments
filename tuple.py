fruits=("Apple","Banana","Grapes","Orange")
print(fruits)
#Accessing tuple element
print(fruits[1])
print(fruits[0:2])

#methods
print(fruits.count("Apple"))
print(fruits.index("Orange"))

#delete element indirect way
a=list(fruits)
a.pop()
fruits=tuple(a)
print(fruits)






