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
	if arr[abs(arr[i])] >= 0:
		arr[abs(arr[i])] = -arr[abs(arr[i])]
	else:
		print (abs(arr[i]), end = " ") 
              
