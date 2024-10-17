AmountA= float(input("Please enter the amount of your first purchase: "))
AmountB= float(input("Please enter the amount of your first purchase: "))
AmountC= float(input("Please enter the amount of your first purchase: "))
Total = AmountA + AmountB + AmountC

print("Your Total Purchase is:", Total, "pesos")

# Purchasing and Loyalty points 
if Total> 100:
   DiscTotal= Total*0.10
   NewTotal= float(Total - DiscTotal)
   NewTotal_rounded= round(NewTotal, 2)
   print("Congratulations, you are qualified for a discount!")
   print("Your NEW TOTAL is:", NewTotal_rounded)
   Loyaltypoints = float(Total/10) 
   Loyaltypoints_rounded= round(Loyaltypoints, 2)
   print("You have earned", Loyaltypoints_rounded, "loyalty points")
   
else:
    print("You may purchase items more than 100.00 pesos to qualify for loyalty points and discount.")
    print("Thank you for puchasing!")

Payment= float(input("Please enter the amount that you'll pay: "))

# Payment
if Payment > NewTotal: 
    Change= float(Payment - NewTotal)
    print("I receieved", Payment, ".", "This is your change:", Change ) 
    print("Thank you!")
    
elif Payment == NewTotal: 
    print("I have received the exact amount. Thank you for Purchasing")
    print("Thank you!")
    
elif Payment<NewTotal:
    print("Your transaction will not proceed. Please pay an exact or greater amount.")
    print("Thank you!")

    