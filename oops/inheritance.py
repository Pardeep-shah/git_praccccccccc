
class parent:
     x = 10
     _y = 20
     __balance =30

     def __init__(self):
          pass
     
     def first(self):
          print("this is my first fucniton ")
    
     print("the value of x is : ", x)
     print("the value of y is : ", _y)
     print("the value of z is : ", __balance)

class child(parent):
     print("--------------------------")


obj = child()

print("starteddddddddddd")
obj.first()
print(obj.x)
print(obj._y)
# print(obj.__balance)




