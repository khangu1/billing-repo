
 # Question 2:
# Create a program for a delivery service that determines shipping status and cost.
# Conditions:
# - If distance < 5km:
#   * If weight < 2kg: $5 delivery fee
#   * If weight 2-5kg: $8 delivery fee
#   * If weight > 5kg: $12 delivery fee
# - If distance 5-10km:
#   * If weight < 2kg: $8 delivery fee
#   * If weight 2-5kg: $12 delivery fee
#   * If weight > 5kg: $15 delivery fee
# - If distance > 10km:
#   * Add $5 to all above rates
#
# Also check if:
# - If it's raining: Add $2 surcharge
# - If it's a holiday: Add 20% to final price
#
# Write a program that calculates delivery fee based on these conditions.

distance=str(input("how far is the place"))
weight=str(input("how heavy is your package"))
weather=str(input("is it raining"))
holiday=str(input("is today a special holiday"))
raining_charges=2
holiday = final_price*0.2



 