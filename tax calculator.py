print("-------------------------------")
print ("Please enter your purchase amount;")
x=input()
print("please enter your tax percentage as an integer;")
t=input()
t=int(t)/100
print("Thank you!")
while float(x)>0:
   tax= float(x)*float(t)
   total= float(x)-float(tax)
   print(float(x),"-",float(tax),"tax","=",float(x)-float(tax))
   print("After taking of taxes you should get back",float(total),"$")
   print("-------------------------------")
   print ("Please enter your purchase amount")
   x=input()
   

