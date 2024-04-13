exp = input("Expression: ")
x,y,z = exp.split(" ")
if y == "+":
    print(float(x)+float(z))
elif y == '-':
    print(float(x)-float(z))
elif y == '/':
    print(float(x)/float(z))
elif y == '*':
    print(float(x)*float(z))