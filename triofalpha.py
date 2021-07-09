'''
Example Input:
t= 2
n= 3
n= 5

Output:
A
BB
CCC
A
BB
CCC
DDDD
EEEEE

'''
t = int(input())
for _ in range(1, t+1):
    n = int(input())
    for i in range(1, n+1):
        for j in range(1, i + 1, 1):
            print(chr(ord('A') - 1 + i), end='')
        print()
