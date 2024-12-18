'''Write a python function to remove a given word from a list and strip it at the same time '''

def remove(list, word):
    new_list = []
    for item in list:
        if not(item==word):
            new_list.append(item.strip(word))
    return new_list
        
list = ['yash', 'nandini', 'anand', 'aditya', 'parth', 'an']
print(remove(list, 'an'))

#or

def remove(list, word):
    return [item.strip(word) for item in list if not(item==word)]

list = ['yash', 'nandini', 'anand', 'aditya', 'parth', 'an']
print(remove(list, 'an'))
