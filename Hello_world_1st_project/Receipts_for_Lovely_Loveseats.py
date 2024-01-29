#Here I'm creating a varaible of store name and assigning some discription to it.
lovely_loveseat_description = 'Lovely Loveseat. Tuffed polyester blend on wood.\n32 inches high x 40 inches wide x 30 inches deep.Red or White.\n\n'

#creating lovely loveseat price variable and assigning value
lovely_loveseat_price = float(254.00)
#Adding new charecteristic piece of furniture!and adding new variable
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.\n\n'

#creating stylish settee price variable

stylish_settee_price = float(180.50)

luxurious_lamp_description = 'Luxurious Lamp. Glass and iron.\n36 inches tall. Brown with cream shade.\n\n'
luxurious_lamp_price = float(52.15)

#creating store variable
sales_tax = float(0.088)

#frist Customer
customer_one_total = float(0.00)
customer_one_itemization = ''
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax =  customer_one_total * sales_tax
#customer one total with inclusive of sales tax  
customer_one_total +=  customer_one_tax

print('Customer One Items\n')
print(customer_one_itemization)
print('Customer One Total : \n')
print(customer_one_total)
