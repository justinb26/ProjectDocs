################################################################
## Let's initialize some variables
myboolean = False
myinteger = 33
myfloat   = 55.35
mystring  = "Hello World"
myplaceholder = None
mylist    = [myboolean, myinteger, myfloat, mystring, myplaceholder]

################################################################

print("\nCombining integers and floats results in a float")
mynewfloat = myinteger + myfloat
print(mynewfloat) ## 88.35
print(type(mynewfloat))

################################################################

print("\nChanging a variable will not change it after it's been added to the list")
myboolean = True
print(myboolean)
print(mylist)

################################################################

print("\nThis isn't true for objects (and lists-within-lists) though")
mynewlist = [1,2,3]     ## Initialize a new list, that we will nest inside
mylist.append(mynewlist)## Add our new list to the original list
mynewlist.append(4)     ## Add another number to our new list
print(mylist)           ## mynewlist is an object, so the changes affect mylist

################################################################

print("\nAdding strings concatenates them\n")
print(mystring + "!!!") 

################################################################

print("\nAdding numbers and strings won't work, must convert first")
#print(mystring + myinteger)
print(mystring + str(myinteger))

################################################################

print("\nWe can also change the type of a variable after it's been assigned")
myinteger = str(myinteger)
print(mystring + myinteger)

################################################################
