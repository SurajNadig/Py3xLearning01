# Multiple Inheritance

class Father:
    def father_money(self):
        return "5"

    def home(self):
        return "This is from the Father"


class Mother:
    def mother_money(self):
        return "2"

    def home(self):
        return "This is from the Mother"


class Son(Father, Mother):
    pass


# Probelm - Diamond Problem - Java
# Python - Multiple Inheritance
# F,M -> S

son = Son()
print(son.father_money())
son.mother_money()
print(son.home())  # Method Resolution - if home fn is there in son class, it will take
# Local prefernce or it will take from first arugment whatever.

# -------------------------------------------------------------------

# class A:
#     def method(self):
#         return "Method A"
#
# class B:
#     def method(self):
#         return "Method B"
#
#
# # class C(A,B):
# #     pass
#
# class C(B,A):
#     pass
#
#
# c = C()
# print(c.method())