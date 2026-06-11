def process_payment():

    subtotal = float(input("Enter the subtotal amount: "))
    location = input("Enter the location of the customer (Urban/Rural): ").upper()
    cupon_code={"CD01","CDO2","CDO3"}
    cupon=input("Enter the cupon code if you have one: ").upper()
    for code in cupon_code:
        if code  in cupon_code:
            if cupon=="CD01":
                discount=subtotal*0.10
                total=subtotal-discount
                print(f"Your total after discount is: Ugx{total:.2f}")
                if location=="URBAN":
                    tax_rate=0.08
                    tax_amount=total*tax_rate
                    total_with_tax=total+tax_amount
                    print(f"Your total after tax is: Ugx{total_with_tax:.2f}")
                elif location=="RURAL":
                    tax_rate=0.05
                    tax_amount=total*tax_rate
                    total_with_tax=total+tax_amount
                    print(f"Your total after tax is: Ugx{total_with_tax:.2f}")
                break
            elif cupon=="CDO2":
                discount=subtotal*0.15
                total=subtotal-discount
                print(f"Your total after discount is: Ugx{total:.2f}")
                if location=="URBAN":
                    tax_rate=0.06
                    tax_amount=total*tax_rate
                    total_with_tax=total+tax_amount
                    print(f"Your total after tax is: Ugx{total_with_tax:.2f}")
                elif location=="RURAL":
                    tax_rate=0.04
                    tax_amount=total*tax_rate
                    total_with_tax=total+tax_amount
                    print(f"Your total after tax is: Ugx{total_with_tax:.2f}")
                break
            elif cupon=="CDO3":
                discount=subtotal*0.20
                total=subtotal-discount
                print(f"Your total after discount is: Ugx{total:.2f}")
                if location=="URBAN":
                    tax_rate=0.05
                    tax_amount=total*tax_rate
                    total_with_tax=total+tax_amount
                    print(f"Your total after tax is: Ugx{total_with_tax:.2f}")
                elif location=="RURAL":
                    tax_rate=0.03
                    tax_amount=total*tax_rate
                    total_with_tax=total+tax_amount
                    print(f"Your total after tax is: Ugx{total_with_tax:.2f}")
                break
        else:
            print("invalid cupon code.Try again")
            