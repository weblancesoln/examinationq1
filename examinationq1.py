# This part of the program allows you to enter a product and add it to a list
product = []
new_product = []

def enter_product():
    y = input('Please Enter a product name')
    return y

def add_product(product):
    z = enter_product()
    product.append(z)
    add_another_product()


def display_product():
    print(product)


def add_another_product():
    z = input('Enter Y to add another to list or N to exit')
    if z == 'Y':
        add_product(product)
    elif z == 'N':
        display_product()
    else:
        print('invalid input')  
        add_another_product()
add_product(product)


#This part of the program converts uppercase to lower case
def to_lower_case():
    x = 0
    while x < len(product):
        y = product[x].lower()
        new_product.append(y)
        x = x+1
to_lower_case()

# This part of the program allows users to search for a products of their interest.
def search_product():
    x = input('Search for the added product')
    m = x.lower()
    z = 0
    if m in new_product[z]:
        count_item = new_product.count(m)
        total = len(new_product)
        print('Number of', m, 'is: ', count_item)
        print('Total item in product is: ', total)
    else:
        print('item not found')
    
search_product()

def to_lower_case():
    x = 0
    while x < len(product):
        m = product[x].lower()
        new_product.append(m)
        x = x+1
to_lower_case()