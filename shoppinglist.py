shopping_list = ['eggs']

def add_item_and_alphabatize(item):
    
    if shopping_list.count(item) == 1:
        print 'This item is already on your shopping list'
    else:
        shopping_list.append(item.lower())
        shopping_list.sort()
 
    return shopping_list

# def alphabatize():
#     shopping_list.sort()
#     return shopping_list

# def remove_item(item):
#     shopping_list.remove(item.lower())
#     return shopping_list

add_item_and_alphabatize('eggs')






