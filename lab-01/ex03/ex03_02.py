def reverse_list(lst):
    return lst[::-1]

input_list = input("Nhap day so: ")
nums = list(map(int, input_list.split(',')))

list_reverse = reverse_list(nums)
print("Reversed List:", list_reverse)