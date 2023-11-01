'''Wap to greet all the person names stored in a
list l1 and which starts with S

l1 = ["Harry","Sahil","Shruti","Rahul"]
'''

l1= ['Harry','Sahil','Shruti','Rahul']

for name in l1:
   # if name[0] == 'S'
    if name.startswith('S'):
        print("Hello !!,"+ name)
