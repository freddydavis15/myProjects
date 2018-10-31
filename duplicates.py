list1=[]
list2=[]
i=0
#input the numbers
number=int(input("how many numbers you have to input"))
for i in range(0,number):
	list1.append(int(input("enter the number")))
print (list1)
#checking the duplicates
for i in range(0, size):
	if list1[(list1[i])] >= 0:
		list1[(list1[i])] = -list1[(list1[i])]
	else:
		list2.append(list1[i])
              
print(list2)
