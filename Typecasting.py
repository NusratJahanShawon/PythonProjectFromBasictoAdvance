#part-02
# typecasting= converting a variable from one to another from one data type to another
#str(), int(), float(), bool()

name="sam"
age=24
gpa=3.31
is_student= True

#printing variables type
type(name)
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# changing one variable to another
age= float(age)
print(age)
print(type(age))

age=str(age)
print(type(age))

gpa=int(gpa)
print(gpa)
print(type(gpa))

name=bool(name)
print(name)

#by using bool we can check if a name or their
#                    variable option is filled up or not like if we
#                    leave a variable empty it will give us false.

# my_name= "sam"
my_name= ""
my_name=bool(my_name)
print(type(my_name))
print(my_name)
