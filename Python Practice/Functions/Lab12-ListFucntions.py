num = [4, 66, 89, 23]


# List is a collection of items
def num_append(suraj_list):  # When we are defining, variable names can be anything, while calling we need to give exact one list list names
    suraj_list.append(100)
    suraj_list[1] = 18
    return (suraj_list)


l = num_append(num)
print(l)


# def num_append2(suraj_list2):  # When we are defining, variable names can be anything, while calling we need to give exact one list list names
#     suraj_list2.append(1023)
#     suraj_list2[1]=14
#     return (suraj_list2)
#
#
# # print(num_append2(num))
# l2 = num_append2(num)
# print(l2)
