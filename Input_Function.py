#input()= a function that prompts the user to
#                       enter data and returns the entered data as a string

name= input("what is your name?")
# age= input("how old are you?")
#-----
# age=int(age)
#-----
#alternative of this can be
age= int(input("how old are you?"))
age=age+1

print(f"hello {name}")
print("Happy Birthday!")
print(f"your age {age} years old.")