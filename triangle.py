#1.a + b > c 
#2.a + c > b 
#3.b + c > a  

list1=[]
for i in range (0,3) :
	list1.append(int(input("enter the side of a triangle")))
print (list1)
if list1[0] + list1[1] > list1[2] :
	if list1[0] + list1[2] > list1[1] :
		if list1[1] + list1[2] > list1[0] :
			print("its a triangle")
else :
	print("its not a triangle")
