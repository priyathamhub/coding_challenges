'''
Some prime numbers can be expressed as Sum of other consecutive prime numbers.

For example
5 = 2 + 3 
17 = 2 + 3 + 5 + 7 
41 = 2 + 3 + 5 + 7 + 11 + 13

Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that
summation should always start with number 2.
Write code to find out number of prime numbers that satisfy the above mentioned property in a given range.
'''

# Each test case contains a number N <= 1000000000
# Print the total number of all such prime numbers which are less than or equal to N.

def isprime(n):
    if(n==1 or n%2==0):
        return 0
    for i in range(3,int(n**0.5)+1, 2):
        if(n%i==0):
            return 0
    return 1

n=int(input())
#since 2 is a prime number 
sum1=2
i=3
count=0
while(sum1<=n):
    if(isprime(i)==1):
        sum1+=i
        if(sum1<=n and isprime(sum1)==1):
            count+=1
    i+=2
print(count)
