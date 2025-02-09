loyalty_card=input("do you have a loyalty card, type yes or no-  ").lower()
tuesday=input("is today tuesday, type yes or no-  ").lower()

bill_amount=int(input("how much is your bill-  "))
discount1=0.2*bill_amount
discount2=0.1*bill_amount
tuesday_discount=0.02*bill_amount
loyalty_card_discount=0.05*bill_amount

if bill_amount>200  :
    if loyalty_card == "yes" and tuesday=="yes":
     final_amount=bill_amount-discount1-tuesday_discount-loyalty_card_discount
     print("you will pay",final_amount, "dollars")
    elif loyalty_card=="no" and tuesday=="no":
        final_amount=bill_amount-discount1
        print("small discount bruvvv",final_amount,"dollars")
    elif loyalty_card=="no" and tuesday=="yes":
      final_amount=bill_amount-tuesday_discount
      print("pay uhmm ",final_amount,"dollars")
    elif loyalty_card=="yes" and tuesday=="no":
        final_amount=bill_amount-loyalty_card_discount  
        print(final_amount,"dollars", "you got a discount bro")
elif 100<=bill_amount<=200  :
    if loyalty_card=="no" and tuesday=="yes":
     final_amount=bill_amount-discount2-tuesday_discount
     print("that will be ",final_amount , "dollars") 
elif 100<=bill_amount<=200  :
    if loyalty_card=="yes" and tuesday=="no":
        final_amount=bill_amount-loyalty_card_discount
        print("that will be ",final_amount, "dollars") 
elif 100<= bill_amount<=200 :
    if loyalty_card=="yes"and tuesday=="yes":
        final_amount=bill_amount-loyalty_card_discount-tuesday_discount
        print("pay uhhh ",final_amount, "dollars" )       
else:
    print("pay ",bill_amount, "dollars please")        
                
         