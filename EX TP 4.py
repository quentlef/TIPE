def aliquote(n):
    a=0
    for i in range(1, n-1):
        if (n%i == 0):
            a = a + i
    return(a)

def estParfait(n): return(aliquote(n)==n)

