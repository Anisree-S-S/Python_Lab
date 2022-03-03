list1 = [3,5,6,7,1,4,6]
list2 = [1,9,0,4,7]

#a. checking length

if(len(list1)==len(list2)):
    print("Lists are of same length")
else:
    print("Lists are not of same length")



#b. checking sums

if(sum(list1)==sum(list2)):
    print("Lists are of same sum")
else:
    print("Lists are not of same sum")

#c. whether any value occur in both
list3 = [value for value in list1 if value in list2]
print("Common values : "+str(list3))