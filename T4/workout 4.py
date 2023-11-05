def Formula(Num):
    if Num == 0:
        return 1
    else:
        return Num * Formula(Num-1)
    
print(Formula(3))