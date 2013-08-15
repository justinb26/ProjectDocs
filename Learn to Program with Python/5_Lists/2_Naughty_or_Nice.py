myname = "Justin"

niceList = []
naughtyList = []

item = None
while item != "":
    item = input("Enter a name for the 'Nice' list. Enter nothing to move on: ")
    if item.strip() != "":
        niceList.append(item)

print("")
print("Ok, moving on to the naughty list.")

item = None
while item != "":
    item = input("Enter a name for the 'Naughty' list. Enter nothing to move on: ")
    if item != "":
        naughtyList.append(item)

## Stacking the deck
if myname in naughtyList:
    naughtyList.remove(myname)
    niceList.insert(0, myname)

print("")

for niceChild in niceList:
    print(niceChild + " has been nice this year. They get a pony.")

for naughtyChild in naughtyList:
    print(naughtyChild + " has been naughty this year. They get a lump of coal.")
