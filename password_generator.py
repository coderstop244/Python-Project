import random

Uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_l=Uppercase_letters.lower()
digits="1234567890"
symbols="(),[],{},*,%,^&.\\,#."
upper,lower,numb,syms=True,True,True,True

all=" "
if upper:
    all+=Uppercase_letters
if lower:
    all+=lower_l
if numb:
    all+=digits
if syms:
    all+=symbols  
length=10
amount=15
for x in range(amount):

    password=" ".join(random.sample(all,length)) 
    print(password)        
