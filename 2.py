lis = ['9','12','-','@','G','#','k','Y','x','78']
upper = []
lower = []
char = []
for h in lis :
    if h.isupper():
        upper.append(h)
    elif h.islower():
        lower.append(h)
    else:
        char.append(h)
print(upper)
print(lower)       
print(char)        