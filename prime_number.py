#Getting user input to find whether it is a prime number or not
n = int(input("Enter a number: "))
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print(test_prime(n))
