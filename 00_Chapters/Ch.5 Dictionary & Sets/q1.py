'''WAP to create a dictionary of Hindi words with values 
as their english translation. Provide user with an option to 
look it up'''

engDict = {
    'Namaste':'Hello',
    'Aapka':'Yours',
    'Kya':'What is that',
    'pyaar':'Love'

}
print("Your options are:",engDict.keys()) # optional
a = input("Enter the Hindi word: \n")
print("The meaning of this word is: ",engDict.get(a))

#or

dict = {
    "ghadi": "Watch",
    "kalam": "Pen",
    "namak": "Salt",
    "haldi": "Turmeric"
}
word = input("Enter the word you want the meaning of: ")
print(dict[word])

