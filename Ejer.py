theList=[]
while True:
    print("MENU")
    print("-------------------")
    print("1.- Add a number to the list")
    print("2.- Add a number in a position in the list")
    print("3.- Show the length of the list")
    print("4.- Delete the last number in the list")
    print("5.- Delete a number in the list")
    print("6.- Count numbers")
    print("7.- Positions of a numbers")
    print("8.- Show the list")
    print("9.- Exit")

    option = int(input("Choose an optione "))
    if option==1:
        num=int(input("Input a number "))
        theList.append(num)
    elif option==2:
        num=int(input("Input a number "))
        pos=int(input("Input a position "))
        if pos <= len(theList):
            theList.insert(pos,num)
        else:
            print("The index is out")
    elif option==3:
        print("the length of the list is: ",len(theList))
    elif option==4:
        if len(theList)>0:
            print("The last element is ", theList.pop(len(theList)-1))   
    elif option==5:
        pos=int(input("Input a position "))
        if pos <= len(theList):
            print("Deleting the element: ", theList.pop(pos))
        else:
            print("The index is out")
    elif option==6:
        num=int(input("Input a number "))
        print("the ocurrences of the number ",num," is ", theList.count(num))
    elif option==7:
        num=int(input("Input a number "))
        index=1
        for elem in theList:
            if elem == num:
                print(index,end=" ")
            index+=1
        print()
    elif option==8:
        for elem in theList:
            print(elem,end=" ")
        print()
    elif option==9:
        break