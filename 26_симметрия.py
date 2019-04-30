number = int(input())
a = number // 1000
b = (number % 1000) // 100
c = (number % 100) // 10
d = number % 10
if (a == d) & (b == c):
    print('1')
else:
    print('0')
