# arr= [1,2,3,4,5]
# arr.reverse()
# print(arr)

array= [2,0,1,2,1,0]
c0=0
c1=0
c2=0
for num in array:
    if num == 0:
        c0+=1
    elif num==1:
        c1+=1
    else :
        c2+=1
while c0!= 0 :
    print("0 ")
    c0-=1
while c1!=0:
                                                                                         
     print("1 ")
     c1-=1
while c2!=0:
    print ("2 ")
    c2-=1

