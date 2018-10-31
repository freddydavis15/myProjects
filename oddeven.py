x=0
list1=[];
list2=[];
list3=[];
#add data in arrray
k=int(input("how many inputs you have to enter?"))
for x in range (0,k):
	list1.append(int(input("enter the number")))
	
print (list1)
#checking odd or even
for data in  list1:
	if data%2==0:
		list2.append(data)
	else : 
		list3.append(data)
print("even")
print (list2)
print("odd")
print(list3)
