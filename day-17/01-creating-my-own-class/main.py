
# > Day 17 -------------------------------------------------------------------------------------------------------------
# > 1. Learning about How to create your own Class ---------------------------------------------------------------------

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# >> 1.1. Learning about Constructors and __init()__ Function ----------------------------------------------------------

user_1 = User(101, "Fabio")
user_2 = User(102, "Isabela")

print(user_1.id, user_1.username, user_1.followers)
print(user_2.id, user_2.username , user_2.followers)

# >> 1.2. Learning about Adding Methods to a Class ---------------------------------------------------------------------

user_1.follow(user_2)
print(f"User_1 | Followers: {user_1.followers} | Following: {user_1.following}")
print(f"User_ 2 | Followers: {user_2.followers} | Following: {user_2.following}")

# ----------------------------------------------------------------------------------------------------------------------