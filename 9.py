n = int(input())
a = n // 100
b = (n % 100 - n % 10) // 10
c = n % 10
print(a)
print(b)
print(c)
print(a + b + c)
