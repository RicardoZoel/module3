mylist=[10,2,3,56,7]
swap=True
while swap:
    swap=False
    for i in range(len(mylist)-1):
        if mylist[i]>mylist[i+1]:
            mylist[i], mylist[i+1]=mylist[i+1],mylist[i]
            swap=True
print(mylist)
print(sorted(mylist))