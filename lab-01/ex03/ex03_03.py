def create_tuple_from_list(lst):
    return tuple(lst)

input_list = input("Nhap day so: ")
nums = list(map(int, input_list.split(',')))

my_tuple = create_tuple_from_list(nums)
print("List:", nums)
print("Tuple tu List", my_tuple)