def CheckIsPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Nhap so can kiem tra: "))

isprime = CheckIsPrime(num)

if isprime:
    print("La so nguyen to")
else:
    print("Khong la so nguyen to")