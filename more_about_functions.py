PI = 3.14

def some_function(x, y, z):
    
    final = x + y + z
    return(final)

output = some_function(5, 6, 7)
# print(output)

def greet_friend(name, sentence, greeting="Hello"):
    output = "{2}, {0}! {1}".format(greeting, name, sentence)
    return(output)

greeting = greet_friend("John", "Hey", "How are you doing today?")
# print(greeting)

def greet_user(greeting):
    user = input("Please enter your name. \n")
    print(type(user))
    print("{}, {}!".format(greeting, user))

    print(5 + int(input("Please enter a integer.")))

greet_user("Hello")