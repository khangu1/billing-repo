secret_number=6
user_input=input("guess the secret number ")
while user_input!=secret_number:
    print("try again")
    user_input=input("guess the secret number")
    if user_input==secret_number:
     break
print ("finally, mate, you got it") 