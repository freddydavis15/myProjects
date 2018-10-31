list1=[]
list4=[]
list2=[]
list3=[]
list5=[]
dict1={}
#inpur the numbers
list1=input("enter the numbers")
list4=list1.split(" ")
#count of space
count=list4.count('')
#removing spaces
for i in range(0,count):
	list4.remove('')
#converting to int
for data in list4:
	list2.append(int(data))
print(list2)
number=len(list2)

for data in list2:
	if data not in dict1:
		dict1[data]=list2.count(data)
		
print(dict1)


