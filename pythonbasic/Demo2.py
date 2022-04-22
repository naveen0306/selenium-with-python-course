# SEQUENCE DATA TYPE
values = [1, 2, "naveen", 4, 5]
# IT IS LIST DATA TYPE AND HOLD MULTIPLE DIFFERENT DATAS

print(values[0])
print(values[2])
print(values[-1])

print(values[0:-1])
values.insert(-1, "vaishnav")
print(values)

values.append("Last one")
print(values)

values[2] = "NAVEEN"
print(values[2])

# tuple is same as list but it is immutable
value_of_tuple = (0, 2, 5, "Ramesh")

# tuple not support any type of changes

# Dictionary
dic = {"a": 5, 4: "dictionary"}

print(dic["a"])
