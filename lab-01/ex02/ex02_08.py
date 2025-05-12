def Divided_By_5(binary_num):
    decimal = int(binary_num, 2)
    if decimal % 5 == 0:
        return True
    else:
        return False
    
binary_str = input("Nhap chuoi nhi phan (cach nhau bang dau phay): ")

binary_list = binary_str.split(',')

numDividedBy5 = [num for num in binary_list if Divided_By_5(num)]

if len(numDividedBy5) > 0:
    result = ','.join(numDividedBy5)
    print("Cac so nhi phan chua het cho 5: ", result)
else:
    print("Khong co so nhi phan nao chia het cho 5")