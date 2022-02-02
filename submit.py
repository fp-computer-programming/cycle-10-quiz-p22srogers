# Author: SMR (AMDG) 2/2/22

prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]

# Question 1:
# First setting the total = 0 as a new variable
# total = 0
# Creating a for loop to go through each value in list of prices
# for price in prices:
# Setting the new variable total = to new variable + value in each index    
# 3 total += price
# Setting a new variable equal to the total / 7 in order to get the average
# total_2=total/7    
# Finally printing out the average
# print(total_2)

# Question 2:
#for price in prices:
#    price-=5
#print(price)

# Question 3:
# Creating a blank list
# products = []
# Using a Zip() command in order to assign each element with one another from each list
# For loop with the zip command
# for num1, num2 in zip(prices, sales):
# Appending the new numbers in the blank list	
#    products.append(num1 * num2)
# Printing out the new list of total values
# print(products)

# Question 5:
# Defining the function to take two arguments
#def add_cloth(price,item):
# Setting x = 0 as a counter   
 #   x = 0
# For the index value in names enumerate    
 #   for i, v in enumerate(price):
# For loop making the ind_2, item_s enumerate the value        
   #     for ind_2, item_s in enumerate(v):
# Update the item to add price            
     #       price[i][ind_2] += " "+ item[x] + "."
 # Set x equal to x + 1           
         #   x += 1
  #  return price
# Updating the prices list 
#prices=add_cloth(prices,items)
# Printing out the result
# print(prices)

# Question 6: 
# First asking inputs of numbers
# enter_number=input("Enter a number: " )
# count=input("What multiple would you like to count by? ")
# Then converting the inputs into integers as new variables. Adding 1 to the variable because range = number -1 
# enter_number_ed=int(enter_number)+1

# count_ed=int(count)

# Creating a for loop in specific range given by inputs above:
# for x in range(0, enter_number_ed, count_ed):
# Printing the numbers    
    # print(x)
