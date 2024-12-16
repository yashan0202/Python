'''What will be the length of the following set S:
S = set()
S.add(20)
S.add(20.0)
S.add("20")'''

S = set()
S.add(20)
S.add(20.0)
S.add("20")
print(len(S))  # Output: 2 , beacuse 20 == 20.0 (interview question)