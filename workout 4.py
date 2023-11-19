def F(num):
    sum = (2**num)+(2*num)
    return sum
def Fp(num):
    sum = (2*num)+2
    return sum
def Sum(num):
    sum = F(num)-(F(num)/Fp(num))
    return sum

print (Sum(8))