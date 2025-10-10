
# > Day 16 -------------------------------------------------------------------------------------------------------------
# > 1. Learning about Constructors and __init()__ Function -------------------------------------------------------------

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User(101, "Fabio")
user_2 = User(102, "Isabela")

print(user_1.id, user_1.username, user_1.followers)
print(user_2.id, user_2.username , user_2.followers)

# ----------------------------------------------------------------------------------------------------------------------