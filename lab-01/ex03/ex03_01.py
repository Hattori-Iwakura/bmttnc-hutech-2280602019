def tong_so_chan(lst):
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
    return sum

input_list = input("Nhap day so: ")
nums = list(map(int, input_list.split(',')))

sum_even = tong_so_chan(nums)
print("Sum of Even:", sum_even)