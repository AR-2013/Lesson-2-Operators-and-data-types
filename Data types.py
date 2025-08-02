name = "Anaira"
age = 11
is_student = True
weight = 40.5

print ("Before Type Casting")
print ("Name :", name)
print ("Data Type of name is:", type(name))
print ("Age :", age)
print ("Data Type of age is:", type(age))
print ("is_student :", is_student)
print ("Data type of is_student is :", type(is_student))
print ("Weight :", weight)
print ("Data type of weight is :", type(weight))

print ("After Type Casting")
weight = int(weight)
print ("Type Cast Of Weight Is :", type(weight))