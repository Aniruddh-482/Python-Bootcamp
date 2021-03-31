# class User:  # Class Creation
#     pass
#     # Prevent the Error(Indentation Expected) of the empty class
#
#
# user_1 = User()
# # Objcet Creation

# # Creating Attributes
# # Attributes of object user_1
# # "An Attribute is an variable that is associated with an object"
# user_1.id = "001"
# user_1.username = "Aniruddh"
# print(user_1.username)

# # Constructor
# # Constructor/Initializing an object
# # Creating a Constructor
# # In Python we can create a constructor by using __init__(self) function
# # Example:
# class Car:
#     def __init__(self):
#         # Initialize Attributes

# # Attributes
# # For Example:
# class Car:
#     def __init__(self, seats):
#         self.seats = seats
# my_car = Car(5)
# # seats = 5

# # For Example:
# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0  # Default Value

# user_1 = User("001", "Aniruddh")  # User_1
# user_2 = User("002", "Yashsavi")  # User_2
# print(user_1.id)
# print(user_1.followers)

# # Creating Methods
# # Methods
# # Attributes are the things that the object has.
# # Methods are the things that the object does.
# # For Example:
# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#
#     def enter_race_mode(self):  # Creating Method
#         self.seats = 2
# my_car = Car(5)
# my_car.enter_race_mode()

# # For Example:
# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
# 
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
# 
# 
# user_1 = User("001", "Aniruddh")  # User_1
# user_2 = User("002", "Yashsavi")  # User_2
# 
# user_1.follow(user_2)  # User_1 starts following User_2
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)
