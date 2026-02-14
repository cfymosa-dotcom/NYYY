print("1. Electricity Bill")
            print("2. Water Bill")
            print("3. Internet Bill")
            print("4. Phone Bill")
            print("5. Other")
            print("--------------------------\n")
            payment_choice = input("Select payment type (1-5): ")
            
            payment_types = {
                "1": "Electricity Bill",
                "2": "Water Bill",
                "3": "Internet Bill",
                "4": "Phone Bill",
                "5": "Other"
            }
            
            if payment_choice in payment_types:
                service_type = payment_types[payment_choice]
                amount = float(input("Enter the amount to pay: "))
                secret = input("Enter secret code: ")
                accounts[account_name].payment(service_type, amount, secret)
            else:
                print("Invalid payment type.")
        else:
            print("Invalid account name.")
    
    elif choice == "5":
        from_account = input("Enter sender account name : ").lower()
        to_account = input("Enter receiver account name : ").lower()
        if from_account in accounts and to_account in accounts:
            amount = float(input("Enter the amount to transfer: "))
            secret = input("Enter secret code: ")
            accounts[from_account].transfer(accounts[to_account], amount, secret)
        else:
            print("Invalid account name(s).")
    
    elif choice == "6":
        print("Exiting... Thank you!")
        break
    
    else:
        print("Invalid option. Please try again.")