#Write a python program with nested decision structures that perform the following: If amount1
#is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2
amount1 = 14
amount2 = 88

if amount1 > 10:
    if amount2 < 100:
        if amount1 > amount2:
           print("greater amount",amount1)
        else:
          print("greater amount",amount2)
    else:
       print("amount2 is not less than 100")
else:
    print("Amount1 is not greater than 10.")             
 
