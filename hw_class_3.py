#----------------for loop--------------
# .......... 1 to 100 addition.....
ans=0
for i in range(1,101,1):
    ans=ans+i
print('Sum is :',ans)

#--------------End--------------------------------

#----List----------------
mylist=['Hasan','Shahin','Bahar']
print(mylist)

print(mylist[2])


mylist.append('Ranga')
print('Append item to list : ', mylist)

mylist.remove(mylist[2])
print('Remove an item from list : ',mylist)

