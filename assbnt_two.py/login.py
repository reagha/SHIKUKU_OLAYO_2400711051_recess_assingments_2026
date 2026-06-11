from admin import weekly_sales_report
from customer import place_order
from cashier import process_payment
def login():
    

    while True:
        print("Please select your role:")
        print("A. Admin")
        print("B.Customer")
        print("C.Cashier")

        role=input("Please select one a letter (A,B,C)").upper()
        print(f"You have selected {role}")
        if role!= "A" and role!="B" and role!="C" :
            print("Invalid choice. Please select A, B, or C.")
        else:
            username=input("Enter your username: ")
            password=input("Enter your password: ")     
            if role == "A" and username=="George" and password=="admin321":
                print("Login successful. Welcome Admin")
                weekly_sales_report()    
                break
            elif role == "B" and username=="Alice" and password=="customer123":
                print("Login successful. Welcome Customer")
                place_order()
                break
            elif role == "C" and username=="Bob" and password=="cashier456":
                print("Login successful. Welcome Cashier")
                process_payment()
                break
            else:
                print("Invalid username or password. Please try again.")



login()

