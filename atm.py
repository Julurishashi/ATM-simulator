print("welcome to mega bank")
Acc_no =[236901,236902,236903,236904,236905]
acc=int(input("enter your account number "))
pin=int(input("enter 4 digit pin"))
acc_bal=10000
for num in Acc_no:
    if acc==num:
        if pin==1234:
            
            print("welcome juluri")
            print("enter options 1.balance 2.deposit 3.withdraw 4.create 5.exit ")
            key=int(input("enter key for above options"))
            if key==1:
                print(f"your acc balance is :{acc_bal} rupees")
            elif key==2:
                amount=int(input("enter amount to deposit")) 
                acc_bal=acc_bal+int(amount)
                print(f"your balance after deposition {acc_bal}")
            elif key==3:
                amount=int(input("enter amount to withdraw"))
                if amount<=acc_bal:
                    acc_bal=acc_bal-int(amount)
                    print(f"amount after withdrawl {acc_bal}")
                else:
                    print("insufficient balance") 
            elif key==4:
                print("your  acc_num is 236908 ")
            elif key==5:
                break   
               
                             
        else:
            print("wrong pin")
           