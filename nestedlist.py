list = []
n = int(input("Enter how many elements in single list : "))
for i in range(0,n):
    elements = int (input())
    list.append(elements)


    x,y = 2,3 
    print ("Enter values for nested list:",x*y) 
    list1 = []
    list2 = []
    for i in range(x):
        for j in range(y):
            list2.append(input())
            list1.append(list2)
            list2 = []

        print("Single list is ")   
        print(list)     
        print("List of list of  is")  
        print(list1)