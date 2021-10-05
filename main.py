class User:
    def __init__ (self,user_id,user_name):
        self.id = user_id # A VARIABLE
        self.name = user_name
        self.followers = 0
        self.following = 0


    def follow(self,user): #THIS IS A METHOD
        user.followers += 1
        self.following += 1
user_1 = User("001","Geetesh")
user_2 = User("002","Angela")

user_1.follow(user_2)

print(user_1.following)
