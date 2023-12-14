import random
def millerRabinTest(n,k):
    r = 1
    d = (n-1)/2
    while (d % 2 == 0):
        print("hi")
        r+=1
        d = d // 2
    #solve for r and d as we go until d is odd, and divide by 2 as 2^r is what we multiply d by
    for _ in range(k):
        #k times as we can run the test as many times as we want
        a = random.randint(2,n-2)
        res = pow(a,d) % n
        if (res == 1) or (res == n-1):
            return True
        #base case if we get a return first example
        for i in range(r-1):
            res = res * res
            if res == 1:
                return False
            if res == n-1:
                return True
        #run until we run out of r, now not base case we know when to return false or true
    return False
    #if we don't get a 1 or n-1 in k attempts, we return false, but should almost never happen

print(millerRabinTest(131,5))