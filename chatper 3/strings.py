name = "rohit"
shortname = name[0:3] # start index included : end index not included
print("2nd character: ", name[1])
print("shortname: ", shortname)
print("length: ", len(name))

# skipping
chars = "abcdefgh"
ans = chars[0:5]
print(ans) # abcde
ans1 = chars[0:5:2]
print(ans1) # ans is ace


#  string functions
len(name)
fullname = "rohit koli"
print(fullname.capitalize())
print(name.startswith("ro"))
print(name.endswith("it"))
print(name.find("0oh"))

# escape characters
name = "hello world\nit is good day"
print(name)

name = "hello world\tit is good day"
print(name)

name = "hello world it is \"good\" day"
print(name)

name = 'hello world it is \"good\" day'
print(name)

name = "This is backslash \\"
print(name)
