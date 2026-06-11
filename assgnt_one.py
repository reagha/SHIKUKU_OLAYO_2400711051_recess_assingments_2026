total_bill=float(input("Enter the total bill amount: Ugx"))
num_people=int(input("Enter the number of people sharing the bill: "))
print("Choose appropriate tip percentage:")
print("option A: 10%")
print("option B: 15%")
print("option C: 20%")
print("option D: Custom tip percentage")

while True:
    tip_option=input("Enter your choice(A,B,C,D):").upper()
    if tip_option=="A":
        tip_percentage=0.10
        break
    elif tip_option=="B":
        tip_percentage=0.15
        break
    elif tip_option=="C":        
        tip_percentage=0.20
        break
    elif tip_option=="D":
        custom_tip=float(input("Enter the custom tip percentage: "))
        tip_percentage=custom_tip/100
        break
    else:
        print("Invalid choice. Please enter A, B, C, or D.")

tip_amount=total_bill*tip_percentage
total_amount=total_bill+tip_amount
amount_per_person=total_amount/num_people

print(f"Total bill amount: Ugx{total_bill:.2f}")
print(f"Tip percentage: {tip_percentage*100:.2f}%") 
print(f"Tip amount: Ugx{tip_amount:.2f}")
print(f"Total amount (bill + tip): Ugx{total_amount:.2f}")
print(f"Amount per person: Ugx{amount_per_person:.2f}")

