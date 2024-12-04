import json, os, re
from time import sleep
from datetime import datetime
from sys import exit



def makeRecord(customer):
    with open(f"general/{customer.customerId}-{customer.name}.json","w",encoding='utf-8') as file:
        json.dump(customer.to_dict(),file,indent=4)


class Customer:
    __customerList = []
    customerId = 1
    def __init__(self, name, id, password, deposit=0,transactions=[]) -> None:
        if deposit < 0:
            raise ValueError("deposit Must Be Greater Or Equal Than 0\n")
        if not re.match(r"^\d{11}$", id):
            raise ValueError("ID Must Be 11 Digits Long")


        self.__name = name
        self.__id = id
        self.__password = password
        self.__balance = deposit
        self.customerId = Customer.customerId
        self.__transactions = transactions
        
        Customer.__customerList.append(self)
        Customer.customerId += 1
        

        if deposit > 0 and transactions == []:
            self.__transactions.append(f"{deposit} GEL Was Deposited On Your Account | Date : {datetime.now()}")

        

        with open(f"general/{self.customerId}-{self.__name}.json","w",encoding='utf-8') as file:
            json.dump(self.to_dict(),file,indent=4)


    def to_dict(self):
        return {
                "Name" : self.__name,
                "ID" : self.__id,
                "Password" : self.__password,
                "Balance" : self.__balance,
                "CustomerID" : self.customerId,
                "Transactions" : self.__transactions
               }
    


    def withdraw(self, amount):

        # Checking Validation
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError("Amount Must Be A Positive Number, Greater Than 0!\n")
        
        if self.__balance < amount:
            raise ValueError("You Do Not Have Enough Money On Your Account.\n")
        
        sleep(0.5)
        print("\nProcessing...\n")
        sleep(1)

        self.__balance -= amount

        print(f"{amount} GEL Is Withdrawed From Account\n")

        self.__transactions.append(f"{amount} GEL Was Withdrawed From Your Account | Date : {datetime.now()}")
        makeRecord(self)



    
    def deposit(self, amount):

        # Checking Validation
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError("Amount Must Be A Positive Number, Greater Than 0!\n")
        
        self.__balance += amount

        sleep(0.5)
        print("Processing...\n")
        sleep(1)

        print(f"{amount} GEL Is Deposited On Your Account")

        self.__transactions.append(f"{amount} GEL Was Deposited On Your Account | Date : {datetime.now()}")
        makeRecord(self)
        

    
    def checkBalance(self):
        sleep(0.5)
        print("Checking Balance...")
        sleep(0.5)

        print(f"Your Balance Is: {self.__balance} GEL\n")
        

    def load_customers(cls, folder_path):
        # Loads all customers from JSON files in the specified folder.
        # Clear existing list
        cls.customerList = []

        # Iterate over all JSON files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".json"):  # Only process JSON files
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r') as file:
                    try:
                        # Load JSON data
                        customer_data = json.load(file)
                        # Create a Customer object and add to the list
                        customer = cls(
                            name=customer_data.get("Name"),
                            id=customer_data.get("ID"),
                            password=customer_data.get("Password"),
                            deposit=customer_data.get("Balance"),
                            transactions=customer_data.get("Transactions")
                        )
                        customer.customerId = customer_data.get("CustomerID")
                        cls.customerList.append(customer)
                    except json.JSONDecodeError as e:
                        print(f"Error reading {filename}: {e}")


    @classmethod
    def get_customerList(cls):
        return cls.__customerList

    @property
    def name(self):
        return self.__name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def password(self):
        return self.__password
    
    @property
    def transactions(self):
        return self.__transactions
    
    def transactions(self, value):
        if isinstance(value, list):
            self.__transactions = value
        else:
            raise ValueError("Transactions must be a list.")
    
    @property
    def balance(self):
        return self.__balance
    

def startMenu():
    return input("1 - ავტორიზაცია\n"
                 "2 - რეგისტრაცია\n"
                 "EXIT - სისტემიდან გამოსვლა\n"
                 "აირჩიეთ: ")

def registrationMenu():
    lst = []
    lst.append(input("შეიყვანეთი თქვენი სახელი და გვარი(მაგალითად: დათო სურგულიძე): ").strip())
    ID = input("შეიყვანეთ თქვენი პირადი ნომერი(ID): ")
    for customer in Customer.get_customerList():
        if customer.id == ID:
            print("მომხმარებელი შეყვანილი პირადი ნომრით უკვე არსებობს.")
            exit()
    lst.append(ID)
    lst.append(input("შეიყვანეთ პაროლი: "))
    lst.append(eval(input("შეიყვანეთ შესატანი თანხა(შეგიძლიათ ჩაწეროთ 0): ")))

    return lst

def authorizationMenu():
    ID = input("შეიყვანეთ თქვენი ID: ")
    return [input("შეიყვანეთ თქვენი პაროლი: "), ID]

def mainMenu():
    return input("1 - ბალანსის შემოწმება\n"
                 "2 - თანხის შეტანა\n"
                 "3 - თანხის გამოტანა\n"
                 "EXIT - სისტემიდან გამოსვლა\n"
                 "აირჩიეთ: ")

if __name__ == "__main__":
    os.makedirs("general",exist_ok=True)
    Customer.load_customers(Customer,"general")
    while True:
        ans = startMenu()
        if ans in ["1","2","EXIT"]:

            if ans == "1":
                while True:
                    answers = authorizationMenu()
                    for customer in Customer.get_customerList():
                        if customer.id == answers[1] and customer.password == answers[0]:
                            while True:
                                newAns = mainMenu()
                                if newAns == "1":
                                    customer.checkBalance()
                                
                                elif newAns == "2":
                                    while True:
                                        try:
                                            customer.deposit(eval(input("შეიყვანეთ თანხა: ")))
                                            break
                                        except:
                                            print("შეცდომა! სცადეთ თავიდან...\n")
                                            sleep(0.5)
                                            continue

                                elif newAns == "3":
                                    while True:
                                        try:
                                            customer.withdraw(eval(input("შეიყვანეთ თანხა: ")))
                                            break
                                        except:
                                            print("შეცდომა! სცადეთ თავიდან...\n")
                                            sleep(0.5)
                                            continue

                                elif newAns == "EXIT":
                                    exit()

                                else:
                                    print("შეცდომა! სცადეთ თავიდან...\n")
                                    sleep(0.5)
                    else:
                        print("პირადი ნომერი ან პაროლი არასწორია.\n")
                    break
                        


            elif ans == "2":
                while True:
                    answers = registrationMenu()
                    print("\n")
                    temp = Customer(*answers)
                    while True:
                        newAns = mainMenu()
                        if newAns == "1":
                            temp.checkBalance()
                            
                        elif newAns == "2":
                            while True:
                                try:
                                    temp.deposit(eval(input("შეიყვანეთ თანხა: ")))
                                    break
                                except:
                                    print("შეცდომა! სცადეთ თავიდან...\n")
                                    sleep(0.5)
                                    continue

                        elif newAns == "3":
                            while True:
                                try:
                                    temp.withdraw(eval(input("შეიყვანეთ თანხა: ")))
                                    break
                                except:
                                    print("შეცდომა! სცადეთ თავიდან...\n")
                                    sleep(0.5)
                                    continue

                        elif newAns == "EXIT":
                            exit()

                        else:
                            print("შეცდომა! სცადეთ თავიდან...\n")
                            sleep(0.5)

            else:
                exit()
        else:
            print("უნდა შეიყვანოთ ან 1, ან 2, ან EXIT\n")