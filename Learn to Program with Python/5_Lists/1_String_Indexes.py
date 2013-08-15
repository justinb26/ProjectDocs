spaceindex = -1

while spaceindex == -1:
    myname = input("Enter your first and last name: ")
    firstletter = myname[0]
    spaceindex = myname.find(' ')

lastname = myname[spaceindex+1::]

print("Hello " + firstletter + " " + lastname)