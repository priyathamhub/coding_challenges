#pattern- 1
'''
Example Input:
t= 2
n= 10

Output:
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2

Example Input:
t= 4
n= 2

Output:
1 1
2 2
3 3
4 4
'''

t = int(input())
n = int(input())
for i in range(1, t+1):
    for j in range(1, n+1):
        print(i, end=" ")
    print()
