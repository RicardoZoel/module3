mylist=[10,2,3,4,4,4,3,3,3,56,7]
newlist=[]
for item in mylist:
    if item not in newlist:
        newlist.append(item)

print(newlist)