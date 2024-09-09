import mysql.connector
import time
import datetime

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sql@123",
    database="bank"
)
bank_name="Indian Bank"

#create account
def create_account(name,phone_no,aadhar_no,address,DOB,account_no,balance):
    cursor=mydb.cursor()
    sql="insert into user_details values(%s,%s,%s,%s,%s,%s,%s)"
    values=(name,phone_no,aadhar_no,address,DOB,account_no,balance)
    cursor.execute(sql,values)
    mydb.commit()
    print(f"{name}, your account was created successfully!...")
    print(f"Your account number is {account_no} ")
    cursor.close()
    
#deposited amount
def deposit(amount,account_no):
    cursor = mydb.cursor()
    sql = "UPDATE user_details SET balance = balance + %s WHERE account_no = %s"
    values = (amount, account_no)
    cursor.execute(sql, values)
    mydb.commit()
    print(f"{amount} was deposited successfully!")
    print(datetime.datetime.now())
    cursor.close()
    

#withdraw amount
def withdraw(amount,account_no):
    cursor = mydb.cursor()
    cursor.execute("SELECT balance FROM user_details WHERE account_no = %s", (account_no,))
    result = cursor.fetchone()
    if result:
        current_balance = result[0]
        if current_balance >= amount:
            new_balance = current_balance - amount
            cursor.execute("UPDATE user_details SET balance = %s WHERE account_no = %s", (new_balance, account_no))
            mydb.commit()
            print(f"{amount} withdrawn successfully!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found.")
    cursor.close()
   

#check bank details
def balance(account_no):
    cursor = mydb.cursor()
    sql = "SELECT balance FROM user_details WHERE account_no = %s"
    cursor.execute(sql, (account_no,))
    result = cursor.fetchone()
    if result:
        print(f"Your current balance is: {result[0]}")
    else:
        print("Account not found.")
    cursor.close()

#correction
def correction(account_no, column_name, new_value):
    cursor = mydb.cursor()
    sql = (f"UPDATE user_details SET {column_name} = %s WHERE account_no = %s")
    values = (new_value, account_no)
    cursor.execute(sql, values)
    mydb.commit()

    print(f"Updated {column_name} for account {account_no} successfully!")
    cursor.close()


while True:
    print()
    print(f"Welcome to {bank_name}")
    time.sleep(0.5)
    print()
    print("1.create account")
    print("2.deposit amount")
    print("3.withdraw amount")
    print("4.Check Balance")
    print("5.Correction")
    print("6.Exit")
    print()
    choice=int(input("Enter your choice(1-6): "))
    if(choice==1):
        name=input("Enter your name: ")
        phone_no=int(input("Enter your mobile no: "))
        aadhar_no=int(input("Enter your aadhar no: "))
        address=input("Enter your address: ")
        DOB=input("Enter your DOB(yyyy-mm-dd): ")
        account_no=input("Enter your account no: ")
        balance=0.0
        
        #call the account creation function
        create_account(name,phone_no,aadhar_no,address,DOB,account_no,balance)

    elif(choice==2):
        amount=float(input("Enter deposited amount: "))
        account_no=input("Enter your user account_no: ")
        deposit(amount,account_no)

    elif(choice==3):
        amount=int(input("Enter your amount: "))
        account_no=input("Enter your account_no: ")
        withdraw(amount,account_no)

    elif(choice==4):
        account_no=float(input("Enter your account_no: "))
        balance(account_no)

    elif(choice==5):
        account_no=input("Enter your account no: ")
        column_name=input("Which data you want to corrected?\n(Eg. name,phone_no,aadhar_no,account_no,DOB,address: ")
        new_value=input("Enter your correction value: ")
        correction(account_no,column_name,new_value)

    elif(choice==6):
        print("Thank you for using the Banking system.\nHave a great day!...")
        break
        
    else:
        print("Invalid choice\nplease enter choice(1-5)")
        
