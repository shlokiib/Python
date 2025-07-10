# que operations - debit, credit 
# acc your bank baalance , 10,000> 7, 20,000> 7.5, 50,000> 8
# exit function 
# any point balance
#  1 credit
#  2 debit
#  3 amount of interest on bal ( simple interest calculator )
#    4 balance current
#    5 exit


def inp(n:int):
        pass
def credit(cred:int,bal:int) :
      if bal>=cred:
        bal = bal -cred 
        print(f"You have credited {cred} credits ")
        
        return getbal(bal)
      else:
       return creditinvalid
def debit (n:int,bal:int) -> int :
        bal = bal + n
        print(f"You have debited {n} credits ")
        return getbal(bal)
def interest(bal:int,year:int) -> int :
        if bal>= 10000:
                ans = bal*year*interest1
                return ans//100
        elif bal>=20000:
                ans = bal*year*interest2
                return ans//100
        elif bal>= 50000:
                ans = bal*year*interest3
                return ans//100
        else:
                return "Balance too low for interest"

        
def getbal(bal:int) :
        newbal = bal
        return newbal
def exit (n:int):
        return exit == True          
              
             
exit = False
bal = 50000
while exit == False :
    creditinvalid = "Unable to Withdraw, Balance less than credited amount"               
    
    interest1,interest2,interest3=7,7.5,8
  
    print("1 Credit")
    print("2 Debit")
    print("3 Amount of interest on bal ( simple interest calculator )")
    print("4 Balance current")
    print("5 Exit")
    oper = int(input("What operation would you like to do "))
    inp(oper)
    if oper == 1:
       cred = int(input("How much would you like to credit "))  
       bal = credit(cred,bal)    
       print ("Your current balance is", bal)
    elif oper == 2:
        deb = int(input("How much would you like to debit "))
        bal = debit(deb, bal)

    elif oper ==3:
        print(f"Your current bal is {bal}")
        inter = int(input("How many year interest would you like to calculate: "))
        print (f"Your interest for {inter} years is "   )
        print (interest(bal,inter))
        temp = bal + interest(bal,inter)
        
        print (f"After {inter} years your balance would be ", temp)
        
    elif oper ==4:
        print("Your current bal is : ",getbal(bal))
        
    elif oper ==5:
        exit = True

print("Thank you for using our bank :) ")