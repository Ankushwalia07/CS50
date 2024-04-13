camel = input("CamelCase: ")
res = ''
for i in camel:
    if(i.isupper()):
        res+="*"+i
    else:
        res+=i
print(res)
x=res.split("*")
result = '_'.join(x)
result = result.lower()

print(result)