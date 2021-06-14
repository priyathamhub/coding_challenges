'''
A prime number is a number that is divisible by only two numbers, 1 and itself. 1 is neither a prime number nor a composite number.
Hence, 2 is the first prime number, 3 is the second prime number and so on..
Your task is to write a program that takes as input an integer N and prints the Nth prime number
'''

# Input consists of a single integer N
# Print the Nth prime number

def is_prime(num):
    for i in range(2, int(num**(0.5))+1):
        if(num % i == 0):
            return False
    return True
def sop(n):
    if n == 1:
        return 2
    count = 1
    num = 3
    while(count <= n):
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 2
print(sop(int(input())))
