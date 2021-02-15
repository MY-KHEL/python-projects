customerName = input('Please input your Name: ').capitalize()
print()

#Beginning of the Phone Number Session

customerPhone = str(0)
while len(customerPhone) != 11 :
    customerPhone = str(input('Please input your Phone Number: '))
    if len(customerPhone) != 11 :
        print('Number must be 11 digits')
    if customerPhone[0]!= '0':
        print('Number must start from 0')
           
    while customerPhone[0]!= '0':
        customerPhone = str(input('Please input your Phone Number: '))
        if customerPhone[0]!= '0':
            print('Number must start from 0')
        if len(customerPhone) != 11 :
            print('Number must be 11 digits')

    print()
print('Lets move on')

print()

#End of the validation of the Phone number

#Starting with the Email aspects:

customerEmail = input('Enter your email: ')
while('@gmail.com' or '@hotmail.com' or '@yahoo.com') not in customerEmail:
    customerEmail = input('Your email address must have @gmail.com or @hotmail.com or @yahoo.com \n')

print('_'*40)
print()

item = {'rice':240,'beans':120,'egg':50,'biscuit':10,'beef':400,'drink':100}
print('Welcome to Mykhel Stores')
print()
print('This is what we have in store and their prices. Choose your order from the items below')


print(item)

    

    
n = int(input('\n How many Goods are you buying: '))

purchase = {}
for i in range(n):
    itemName = input('Enter your Order \n').lower()
    while itemName not in item.keys():
        itemName = input('We dont have that in store, check the Store for items we have \n').lower()
        print()
    itemQuantity = int(input('How many of this product are you buying: '))
    itemPrice = item[itemName] 
    totalPrice = str(itemPrice*itemQuantity)
    print('Price for one : ',itemPrice)
    print('Price for ',itemQuantity,': ',totalPrice)
    
    purchase[itemName]=itemQuantity 
    
    i += 1
    
totalValue = {}
print()
print('_'*100)
print()
print('Get your Invoice')
print()
print('Name: ',customerName)
print()
print('Phone Number: ',customerPhone)
print()
print('Email: ',customerEmail)
print()
print('Keep shopping at Mykhel Stores')
print('_'*40)
print('Item',' '*9,'Qty',' '*7, 'Total')
print()
for key, value in purchase.items():
    print(key, '-' * 10, value, '-' * 10, value * item.get(key))
    totalValue[key] = value * item.get(key)
print(' ' * 40)
print('Total', '-' * 22, sum(total_value.values()))
print('\n Thank you for Shopping with us!')