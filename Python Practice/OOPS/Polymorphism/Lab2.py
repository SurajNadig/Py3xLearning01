class father:
    def home(self):
        print("1BHK")

class son(father):
    def home(self):
        super().home() # super means call my parent function
        print("3BHK")

s1=son()
s1.home()

