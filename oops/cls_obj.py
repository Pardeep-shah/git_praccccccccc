# x = 10
# print(x)

# print("starting ")

# # funcion  definition 

# def myfxn():
#     x = 10
#     print("the value of x is : ", x)

# # fxn calling 

# myfxn()


# class parent:
#      x = 10

#      def __init__(self):
#           pass
     
#      def first(self):
#           print("this is my first fucniton ")

# obj = parent()
# print("class fxnlity started")
# obj.first()
# print(obj.x)
# print("khjlll;")
# # print(x)




# encapsulation 

class parent:
     x = 10
     _y = 20
     __z =30

     def __init__(self):
          pass
     
     def first(self):
          print("this is my first fucniton ")
    
     print("the value of x is : ", x)
     print("the value of y is : ", _y)
     print("the value of z is : ", __z)


obj = parent()
print("class fxnlity started")
obj.first()
print(obj.x)
print("==========================================")

print("the value of x is : ", obj.x)
print("the value of y is : ", obj._y)
# print("the value of z is : ", obj.__z)

