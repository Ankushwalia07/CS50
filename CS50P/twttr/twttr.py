string = input("Input: ")
vow = ["A" ,"E" ,"I", "O", "U", "a", "e", "i", "o", "u"]
output = print("Output: ")
for s in string:
     if s.casefold() not in vow:
          print(s,end = "")
print()
