# Extracting ovels using for loops method 1:
# ovels=['a','e','i','o','u']
# ovels_list=[]
# for let in letters:
#     if let in ovels:
#         ovels_list.append(let)
# print(ovels_list)

# #Extracting ovels using for loops method 2:
# ovels='aeiou'
# ovels_list=[]
# for let in letters:
#     if let.lower() in ovels:
#         ovels_list.append(let)
# print(ovels_list)
letters = ['a', 'r', 'i', 'p', 'o', 'u', 'n', 'e', 'l']


def ovels_func(let):
    ovels = ['a', 'e', 'i', 'o', 'u']
    return let in ovels


# print(ovels_func('u')) #It Return True or false since IN is used ovels_func function

filtered_ovels = filter(ovels_func, letters)
print(list(filtered_ovels))
