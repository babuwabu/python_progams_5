# ask user full name
fullname =input("Enter your full name: ")
# print name in pascal case
print(''.join(word.capitalize() for word in fullname.split()))