list1=["mmd","rn",]
y = list1[::-1]
for x in y:
    for k in list1:
        if(x == k):
            txt="tru"
        else:
            txt = "fals"
print(txt)