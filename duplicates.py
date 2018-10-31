list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
i=0
#input the numbers
list1=input("enter the numbers")

list4=list1.split(" ")

count=list4.count('')
for i in range(0,count):
	list4.remove('')
#print (list4)

for data in list4:
	list2.append(int(data))
print(list2)

number=len(list2)

#checking the duplicates
for data in list2:
	if data not in list5:
		list3.append(list2.count(data))
		list5.append(data)
#print(list3)
#print(list5)

for data in list3:
	list6.append(int(data/2))
#print(list6)

print(sum(list6))
