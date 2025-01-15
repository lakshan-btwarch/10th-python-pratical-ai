# Code to check character type
character = input("Enter any character: ")

if character.isupper():
    print(f"{character} is an uppercase letter.")
elif character.islower():
    print(f"{character} is a lowercase letter.")
elif character.isdigit():
    print(f"{character} is a digit.")
elif character.isspace():
    print(f"{character} is a space.")
else:
    print(f"{character} is a special character.")
