d={'pen':20,'pencil':10,'eraser':5,'scale':10}
item=input('Enter the item name :')
try :
    print(d[item])
except KeyError :
    print('Item not found!')