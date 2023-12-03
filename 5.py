lis = ['8','a','g','t','j','8','7']
print (lis)
for a in lis[::]:
    lis.pop(0)
print(lis)
#####################
lis2 = ['8','a','g','t','j','8','7']
print (lis2)
for a in lis2[::]:
    del lis2[0]
print(lis2)
#######################
lis3 = ['8','a','g','t','j','8','7']
print (lis3)
for a in lis3[::]:
    lis3.remove (a)
print(lis3)
