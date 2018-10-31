#enter the numbers
list1=input("enter the numbers")
print (list1)

list2=list1.split(" ")
print (list2)
count=list2.count('')
for i in range(0,count):
	list2.remove('')
print (list2)
number=len(list2)
i=0
j=0
for i in range (0,number):
	for j in range(0, i+1):
		print(list2[j],end=" ")
	print("\r")
