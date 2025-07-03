# for i,v in enumerate(['x','y','z','a','b']):
#     print(i,v)



m= [[10,20,30],[40,50,60],[70,80,90]]
# print(m)
res=0
for row in m:
    print(row)
    
for i in range(3):
    for j in range(3):
        res += m[i][j]
    

print(res)        