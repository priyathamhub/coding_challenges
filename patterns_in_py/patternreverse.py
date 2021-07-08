#pattern- 3
# Print the reverse of number pattern
'''
Input:
5
Output:
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''
n = int(input())
lst = []
for i in range(n, 0, -1):
    lst.append(i)
    print(*lst)
