# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 18:04:47 2024

@author: Anupam Nair
"""
import mysql.connector as sqltor

mycon=sqltor.connect(host="localhost",user="root",passwd="Anupam@123",database="banking")

if mycon.is_connected()==False:
    print("error")

cursor=mycon.cursor()

print(" Hello, Welcome to Banking ! Please enter your user credentials below ")

user_name=input("enter name : ")
password=input("enter password : ")
inp=(user_name,password)

st="select balance from bank_details where f_name=%s and password=%s"
cursor.execute(st,inp)
data=cursor.fetchall()

if data:
    print("user verified! You can proceed")

    def deposit():
        amount=int(input("enter a amount to deposit "))
        if amount<0:
            print("please enter a valid amount to enter")
            return 0
        else:
            return amount
    def withdraw():
        amount=int(input("enter amount to withdraw : "))
        if amount<0:
            print("please enter a valid amount to enter ")
            
            return 0
        else:
            return amount
        

    
      
    
    balance=int(data[0][0])
    is_run=True
    
    
    while is_run:
            
        print("    BANKING PROGRAM   ")
        print("1.Deposit ")
        print("2.Withdraw")
        print("3.Show Balance")
        print("4.Exit")
        choice=int(input("enter a choice (1 -4 ): ") )
        if 1<=choice<=4:
            if choice==1:
                    value=deposit()
                    
                    
                    
                    if value>0:
                        balance+=value
                    
                        st1="UPDATE bank_details SET balance=%s WHERE password=%s"
                        inp=(balance,password)
                        
                        cursor.execute(st1,inp)
                        
                        mycon.commit()
                        
                        print("After depositing,this is the balance :",balance)
                    else:
                        print("no amount deposited")
                       
                       
                
            elif choice==2:
                value=withdraw()
                if value>balance:
                    print("Withdraw amount exceeds balance. please exit or enter new")
                else:
                    balance-=value
                    st1="UPDATE bank_details SET balance=%s WHERE password=%s"
                    inp=(balance,password)
                    
                    cursor.execute(st1,inp)
                    
                    mycon.commit()
                    
                    print("the amount of ",value,"has been withdrawn and the balance after is ",balance)
                    
            elif choice==3:
                
                print("Your balance is : ",balance)
                
            else:
                
                is_run=False
                
        else:
            
            print("please enter a valid choice between 1 and 4")
        
        print("thank you for banking with us!! Have a Nice Day !!")  
            
else:
    print("invalid! credentials, please try again ")
