#create an empty list called my_list
my_list=[]
#append 10,20,30,40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#print my_list to display the list
print(my_list)

#insert 15 at the second position in the list
my_list.insert(1, 15)
#print the updated list
print(my_list)
#extend my_list with another list: 50,60,70
my_list2=[50,60,70]
my_list= my_list+my_list2
#print the updated list
print(my_list)
#remove the last element on the list
my_list.pop(-1)
print(my_list)
#sort the list in ascending order
my_list.sort()
print(my_list)
#find and print the indexes of 30 in the list
if 30 in my_list:
    index_of_30 = my_list.index(30)
    print("the index of 30 is:", index_of_30)
else:
    print("30 is not in the list")