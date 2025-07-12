# input from users
# total rent
# total food
# elecircity bill 
# charge per unit
# output
# totaL amout pay
# total persons

rent = int(input("enter the total rent = "))
food = int(input("enter the total food = "))
electricity_bill = int(input("enter the electricity bill ="))
charge_per_unit = int(input("enter the charge per unit ="))
persons = int(input("enter the total persons ="))


# calculate the total amount pay
total_amount_pay = electricity_bill * charge_per_unit

output =(food + rent + total_amount_pay)// persons

print(" each person pay is = ",output)  # output the total amount pay

