import math as Formula
def Formu(Num1,Num2,Num3):
    sum = (Num1**2)+(Num2**2)*Num3
    Sq = -Num1+Formula.sqrt(sum)
    return(Sq)
print(Formu(8,1,6))
