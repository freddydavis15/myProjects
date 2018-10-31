#insert number in an array
def enter():
    list1 = []
    
    i=0
    number=int(input("enter the total numbers you want insert"))
    for i in range(0,number) :
        list1.append(int(input("enter the numbers")))
    print(duplicate(list1))

#find duplicates in array
def duplicate(list1):
    list2 = []
    for data in list1: 
        if data not in list2: 
            list2.append(data)             
    #print (list2)
    print ("number of sets in the array is", len(list2))

print (enter())            

