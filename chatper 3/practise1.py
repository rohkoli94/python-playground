#  Q1
name = input("enter name: ")
print(f"Good Afternoon {name} ")

# Q2
letter = '''
Dear <Name>
You are selected
<Date>
'''

newletter = letter.replace("<Name>", name).replace("<Date>", "21st June 2026")
print(newletter)


# Q3 find double space in string
letter = "hello  rohit"
print(letter.find("  "))


# Q4 replace doble space with single space
newletter = letter.replace("  ", " ")
print(newletter)


#  Q5
letter = "Dear Rohit,\n\tthis python course is nice.\nThanks!"
print(letter)
