file = open(r'D:\udemy\pythonbasic\test.txt')
print(file.read(5))
print(file.readline())


line = file.readline()

while line!= "":
    print(line)
    line = file.readline()

file.close()