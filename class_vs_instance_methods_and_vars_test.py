# # class MyClass:
# #     my_var = 10  # class variable
# #
# #     def modify_var(self, new_value):
# #         self.my_var = new_value  # this creates an instance variable, it doesn't modify the class variable
# #
# # # create an instance of MyClass
# # my_instance = MyClass()
# #
# # # call the modify_var method
# # my_instance.modify_var(20)
# #
# # # print the class variable and the instance variable
# # print(MyClass.my_var)  # prints: 10
# # print(my_instance.my_var)  # prints: 20
# #
# # # vs:
#
# print("Now we're changing the modify_var instance method to refer to the class variable")
# class MyClass:
#     my_var = 10
#     def modify_var(self, new_value):
#         MyClass.my_var = MyClass.my_var + new_value  # this modifies the class variable
#
# # create an instance of MyClass
# my_instance = MyClass()
#
# for i in range(1, 10):
#     # call the modify_var method
#     my_instance.modify_var(10)
#
#     # print the class variable
#     print(MyClass.my_var)  # prints: 20
#     print(my_instance.my_var)  # prints: 20
#
#
# print("Now we're gonna try using setters and getters")
# class MyClass:
#     _class_var = 0  # class variable
#
#     def __init__(self):
#         self._instance_var = 0  # instance variable
#
#     @property
#     def instance_var(self):
#         return self._instance_var
#
#     @instance_var.setter
#     def instance_var(self, value):
#         if value >= 0:
#             self._instance_var = value
#         else:
#             raise ValueError("Value must be non-negative")
#
#     @classmethod
#     @property
#     def class_var(cls):
#         return cls._class_var
#
#     @class_var.setter
#     @classmethod
#     def class_var(cls, value):
#         if value >= 0:
#             cls._class_var = value
#         else:
#             raise ValueError("Value must be non-negative")
#
# # create an instance of MyClass
# my_instance = MyClass()
#
# # set and get instance_var
# my_instance.instance_var = 10
# print(my_instance.instance_var)  # prints: 10
#
# # set and get class_var
# MyClass.class_var = 20
# print(MyClass.class_var)  # prints: 20
#
# print("Creating my_instane2")
# # create an instance of MyClass
# my_instance2 = MyClass()
#
# # set instance_var
# my_instance2.instance_var = 10
#
# # get instance_var
# print(my_instance2.instance_var)  # prints: 10
#
# # set instance_var to a new value
# my_instance2.instance_var = 20
#
# # get instance_var again
# print(my_instance2.instance_var)  # prints: 20
#
#

class Animal:
    def sound(self):
        print("Every animal makes a sound. Even giraffes, they make some weird bleating sound.")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("The dog barks. All dogs originally come from the legendary Goodboy Island.")

# create a Dog object
d = Dog()

# call the sound method
d.sound()
