theList = []
def showMenu():
    print("Menu")
    print("1.- Add number")
    print("2.- Add number in a position")
    print("3.- Show the length")
    print("4.- Delete the last number")
    print("5.- Delete a number in the list")
    print("6.- Count number")
    print("7.- Positions of a number")
    print("8.- Show the list ")
    print("9.- Exit")
    option = int(input("Choose an option:"))
    return option
def addNumber():
    num = int(input("Input a number"))
    theList.append(num)

def addNumberAtPos(num, pos):
    if pos <= len(theList):
        theList.insert(pos,num)
        return True
    else:
        return False
def getLastElement():
    if len(theList) > 0:
        return theList.pop()
    
    return False

def deleteAtPos(pos):
    if pos <= len(theList):
        return theList.pop(pos)
    return False

while True:
    option = showMenu()
    if option == 1:
        addNumber()
    elif option == 2:
        num = int(input("Input a number"))
        pos = int(input("Input the position"))
        if addNumberAtPos(num,pos):
            print("Number added correctly!!")
        else:
            print("The index is out!!!")
    elif option == 3:
        print("The length of the list is ",len(theList))
    elif option == 4:
        num = getLastElement()
        if num == False:
            print("The list is empty!!!")
        else:
            print("The last element is ",num)    
    elif option == 5:
        pos = int(input("Input the position"))
        num = deleteAtPos(pos)
        if num == False:
            print("The position does not exist!!!")
        else:
            print("Deleting the element ",num)
    elif option == 6:
        num = int(input("Input a number"))
        print("The ocurrences of the number ",num, " is ", theList.count(num))
    elif option == 7:
        num = int(input("Input a number"))
        pos=0
        for elem in range(0,theList.count(num)):
            index = theList.index(num,pos)
            print(index,end=" ")
            pos = index + 1
        print()
        """index = 1
        for elem in theList:
            if elem == num:
                print(index, end = " ")
            index += 1
        print()   
        """

    elif option == 8:
        for elem in theList:
            print(elem,end=" ")
        print()
    elif option == 9:
        break
