import random
credit=50

print("Hello to my dice rolling sim")

print("if you get a roll that is equal or smaller then 3 \
, you win 10$. If its bigger than 3 , you lose 10$")

reroll=input("Would you like to roll? y/n ;")
while reroll==str("y")and(credit>=10):
       roll=random.randint(1,6,)
       print("You rolled a ;",roll)
       if roll<=3:
              credit=int(credit)+10
              print(credit,"$")
              reroll=reroll=input("Would you like to roll? y/n ;")
       else:
              credit=int(credit)-10
              print(credit,"$")
              reroll=input("Would you like to roll? y/n ;")
print("Bye!, Better luck next time.")
      



        

    




