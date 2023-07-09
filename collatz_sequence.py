n = int(input("Enter Number: "))
def Collatz_Sequence(n):
 result = []
 while n > 1:
    if n % 2 != 0:
        n = (3 * n) + 1
        result.append(n)
    else:
        n = n // 2
        result.append(n)
 return result
print(Collatz_Sequence(n))
