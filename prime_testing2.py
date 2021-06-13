'''
You are given Q different queries. Each query consists of one number each i.e. N. You are to write a program that, for each query tests
whether the number is prime or not. You must output Q different lines to stdout, ith line being "yes" if the N for ith query is a prime
number and "no" otherwise.
'''

# Input: First line contains one integer, the number of queries Q. Next Q lines contain one integer each, the N for the queries.
# Output: print "yes" or "no" depending on the primality of the N in the query.

def fun1(q):
    flag =0
    l = int(input())
    if (l==2):
        return ('yes')
    elif (l%2==0 or l==1):
        return ('no')
    else:
        for j in range(3, int(l**(0.5))+1, 2):
            if (l%j==0):
            #print('no')
                flag =1
                break
            else:
                flag = 0
        if(flag==1):
            return ('no')
        else:
            return ('yes')

qp = int(input())
for i in range(qp):
    print(fun1(qp))
