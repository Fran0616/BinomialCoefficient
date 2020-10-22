#Francisco
#Binomial coefficients are the positive intergers that occurs as coefficients in the binomial theorem 
def binomial(n,k):
    
    if k==0 or k == n:
        return 1
    #Recursive 
    return binomial(n-1, k-1) + binomial(n-1, k)

num = 12
num2 = 5
print("B(",num,",",num2, ")" , "=", binomial(num, num2))
#Output: B( 12 , 5 ) = 792
num = 10
num2 = 7
print("B(",num,",",num2, ")" , "=", binomial(num, num2))
#Output: B( 10 , 7 ) = 120
num = 15
num2 = 9
print("B(",num,",",num2, ")" , "=", binomial(num, num2))
#Output: B( 15 , 9 ) = 5005
