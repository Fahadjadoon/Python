# Bank account management system

#1. Insert pin 
#2. Check balance 
#3. Debit ()
#4. credit()



class Clients:

    def __init__(self):
        
        self.clients = {
        "001":{
            "Name" :"Fahad",
            "Pin" : "1997",
            "Amount" : 90000.0
        },

        "002":{
            "Name" :"Umer",
            "Pin" : "1234",
            "Amount" : 54000.0
        },

        "003":{
            "Name" :"Hassan",
            "Pin" : "7788",
            "Amount" : 700.0
        }      
               }
        
        # Function to handle login
    def Login(self, client_id):
        while True:
            Pin = input("Insert pin: ")
            if Pin == self.clients[client_id]["Pin"]:
                print('You are successfully logged in')
                print(f"Welcome {self.clients[client_id]['Name']}")
                break
            else:
                print('Invalid pin. Please try again.')

        
    def Check_balance(self, client_id):

        print(f"Your Balance is : {self.clients[client_id]['Amount']}")

    def Debit_amount(self, client_id):
        amount = float(input("Please insert the amount you want to withdraw: "))
        if amount <= self.clients[client_id]['Amount']:
            self.clients[client_id]['Amount'] -= amount
            print(f"{amount} is debited from your account")
            print(f"Your current Balance is: {self.clients[client_id]['Amount']}")
        else:
            print("Insufficient funds")

    def Credit_amount(self, client_id):

        amount = float(input("Please insert the amount you want to insert"))

        self.clients[client_id]["Amount"] += amount
        print(f"{amount} is credited in your account")
        print(f"Your current Balance is : {self.clients[client_id]['Amount']}")

c1 = Clients()

client_id = input("Enter Your ID")

c1.Login(client_id)

print("1. Check Balance")
print("2. Widraw Amount")
print("3. Insert Amount")

choice = int(input("Select any option"))

if choice == 1:
    c1.Check_balance(client_id)
elif choice == 2:
    c1.Debit_amount(client_id)
elif choice == 3:
    c1.Credit_amount(client_id)


