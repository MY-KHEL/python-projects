customerName = input('Please input your Name: ')
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

storeItems = {'rice':200,'bread':200,'egg':70,'beans':100,'indomie':40}
print('This is what we have in store , please select from the items below \n', tuple(storeItems))
print()


itemName = (input('The name of the item you are buying ').lower())
itemQuantity = eval(input('What is the quantiy of what you are buying '))
print()
priceForOne = (storeItems[itemName])
tPriceOfProduct = itemQuantity * priceForOne
print('Price for One : ',priceForOne)
print('The total Price of the Product : ',tPriceOfProduct)
    
itemName5 = (input('The name of the item you are buying ').lower())
itemQuantity5 = eval(input('What is the quantiy of what you are buying '))
print()
priceForOne5 = (storeItems[itemName5])
tPriceOfProduct = int(itemQuantity5 * priceForOne5)
print('Price for One : ',priceForOne5)
print('The total Price of the Product : ',tPriceOfProduct5)
    
itemName2 = (input('The name of the item you are buying ').lower())
itemQuantity2 = eval(input('What is the quantiy of what you are buying '))
print()
priceForOne2 = (storeItems[itemName2])
tPriceOfProduct2 = int(itemQuantity2 * priceForOne2)
print('Price for One : ',priceForOne2)
print('The total Price of the Product : ',tPriceOfProduct2)
    
itemName3 = (input('The name of the item you are buying ').lower())
itemQuantity3 = eval(input('What is the quantiy of what you are buying '))
print()
priceForOne3 = (storeItems[itemName3])
tPriceOfProduct3 = int(itemQuantity3 * priceForOne3)
print('Price for One : ',priceForOne3)
print('The total Price of the Product : ',tPriceOfProduct3)
    
itemName4 = (input('The name of the item you are buying ').lower())
itemQuantity4 = eval(input('What is the quantiy of what you are buying '))
print()
priceForOne4 = (storeItems[itemName4])
tPriceOfProduct4 = int(itemQuantity4 * priceForOne4)
print('Price for One : ',priceForOne4)
print('The total Price of the Product : ',tPriceOfProduct4)
    

    
print('Your Total price is ',tPriceOfProduct+tPriceOfProduct2+tPriceOfProduct3+tPriceOfProduct4+tPriceOfProduct5)
