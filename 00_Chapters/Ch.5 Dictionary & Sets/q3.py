''''WAP to create an empty dictionary. Allow 4 friends
to enter their favorite language as values and use keys
as their names. Assume that the names are unique '''

# friends = {}
# friend1_name = input("Enter friend1's name: ")
# friend2_name = input("Enter friend2's name: ")
# friend3_name = input("Enter friend3's name: ")
# friend4_name = input("Enter friend4's name: ")
# language1 = input(f"{friend1_name}'s favorite language is: ")
# language2 = input(f"{friend2_name}'s favorite language is: ")
# language3 = input(f"{friend3_name}'s favorite language is: ")
# language4 = input(f"{friend4_name}'s favorite language is: ")
# friends[friend1_name] = language1
# friends[friend2_name] = language2
# friends[friend3_name] = language3
# friends[friend4_name] = language4
# print(friends)

#or

f ={ }

name = input("Enter friend's name: ")
lang = input(f"{name}'s favorite language is: ")
f.update({name:lang})

name = input("Enter friend's name: ")
lang = input(f"{name}'s favorite language is: ")
f.update({name:lang})

name = input("Enter friend's name: ")
lang = input(f"{name}'s favorite language is: ")
f.update({name:lang})

name = input("Enter friend's name: ")
lang = input(f"{name}'s favorite language is: ")
f.update({name:lang})

print(f)

