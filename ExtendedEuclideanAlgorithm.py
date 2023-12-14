
def EuclidAlgorithm(a,b):
    if b > a:
        while (b-a) >= 0:
            b = b - a
    else:
        while (a-b) >= 0:
            a = a - b
    #figures out which is greater and then reduces the other as much as possible
    if a == 0:
        return b
    if b == 0:
        return a
    # if a or b = 0, that means it's a multiple of the other, so the other is the gcd
    if ((a or b) == 1):
        return 1
    #if a or b is 1 that means 1 is the gcd
    return EuclidAlgorithm(a,b)
    #keep going until we find the gcd

def ExtendedEuclidAlgorithm(x,y, n):
    a = 1
    while (((n-a*x)% y)!= 0):
        a += 1
        #once we know that n-ax % y is 0, that means at by = 0, so we have a
    b = (n-a*x)/y
    #set b to n-ax/y as ax +by =n
    return [a,b]


gcd = (EuclidAlgorithm(15,290))
#gives us our gcd
print(gcd)
print(ExtendedEuclidAlgorithm(15,290,gcd))
#gives us our multiples