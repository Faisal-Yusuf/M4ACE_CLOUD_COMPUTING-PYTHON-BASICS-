USSD_CODE = "*2026#"
last_card_digits = '111999'
Account_Balance = "N300_000_000"
code = input("Input USSD Code(*2026#): ")
if USSD_CODE == code:
    print("WELCOME TO M4ACE BANKING")
    print("1.Transfers \n2>Airtime\n3>Data\n4>Bills Payment\n5>Check Balance\n6>Open Account\n7>Change Pin\n8>Register\n0>Exit\n")

    selection = int(input("Choose your option from 0-8: "))
    # ==================
    # Option 1(Transfer)
    # ==================
    if selection == 1:
        last_card_digits_input = input("Welcome to 2026 M4ACE!\nPlease enter the last six digits of your Debit Card: ")
        pin_creation = int(input("Create Pin: "))
        pin_confirmation = int(input("Please, confirm your pin: "))

        if len(last_card_digits_input) == 6:
            if last_card_digits == last_card_digits_input:
                if pin_creation == pin_confirmation:
                    print("Pin Successfully created")
                    print("\n1>Transfer to M4Ace Bank\n2>Transfer to Other Banks")
                    transferType = input("Transfer Type: ")

                    if transferType.isdigit():
                        transferType = int(transferType)
                        # ==================
                        # Same Bank Transfer
                        # ==================

                        if transferType == 1:
                            beneficiary_num = input("Enter beneficiary account Number: ")
                            if len(beneficiary_num) == 10:
                                amount = int(input("Enter amount: N"))
                                transaction_pin = int(input("Enter 4-digit PIN(default: 0000): "))
                                if transaction_pin == 0000:
                                    transfer_confirmation = input("Confirm transfer(Yes/No): ")
                                    if transfer_confirmation == "Yes":
                                        print(f"\nYou have successfully transferred a sum of {amount} to\nAccount number: {beneficiary_num}")
                                    elif transfer_confirmation == "No":
                                        print("Please, start over again")
                                    else:
                                        print("Please, Enter the correct value")
                                else:
                                    print("Incorrect pin")
                            else:
                                print("Please, enter a valid account number")

                        # =======================
                        # Transfer to other Banks
                        # =======================

                        elif transferType == 2:
                            print("\nBeneficiary banks:\n1>Access Bank\n2>GTB\n3>Polaris bank")
                            beneficiary_bank = input("Select beneficiary bank: ")
                            if beneficiary_bank.isdigit():
                                beneficiary_bank = int(beneficiary_bank)

                                if beneficiary_bank == 1:
                                    beneficiary_num = input("Enter beneficiary account Number: ")
                                    if len(beneficiary_num) == 10:
                                        amount = int(input("Enter amount: N"))
                                        transaction_pin = input("Enter 4-digit PIN(default: 0000): ")
                                        if transaction_pin == 0000:
                                            transfer_confirmation = input("Confirm transfer(Yes/No): ")
                                            if transfer_confirmation == "Yes":
                                                print(
                                                    f"\nYou have successfully transferred a sum of N{amount} to,\nAccount number: {beneficiary_num}\nBank Name: Access Bank")
                                            elif transfer_confirmation == "No":
                                                print("Please, start over again")
                                            else:
                                                print("Please, Enter the correct value")
                                        else:
                                            print("Incorrect pin")

                                elif beneficiary_bank == 2:
                                    beneficiary_num = input("Enter beneficiary account Number: ")
                                    if len(beneficiary_num) == 10:
                                        amount = int(input("Enter amount: N"))
                                        transaction_pin = input("Enter 4-digit PIN(default: 0000): ")
                                        if transaction_pin == 0000:
                                            transfer_confirmation = input("Confirm transfer(Yes/No): ")
                                            if transfer_confirmation == "Yes":
                                                print(
                                                    f"\nYou have successfully transferred a sum of N{amount} to,\nAccount number: {beneficiary_num}\nBank Name: GT Bank")
                                            elif transfer_confirmation == "No":
                                                print("Please, start over again")
                                            else:
                                                print("Please, Enter the correct value")
                                        else:
                                            print("Incorrect pin")

                                elif beneficiary_bank == 3:
                                    beneficiary_num = input("Enter beneficiary account Number: ")
                                    if len(beneficiary_num) == 10:
                                        amount = int(input("Enter amount: N"))
                                        transaction_pin = input("Enter 4-digit PIN(default: 0000): ")
                                        if transaction_pin == 0000:
                                            transfer_confirmation = input("Confirm transfer(Yes/No): ")
                                            if transfer_confirmation == "Yes":
                                                print(f"\nYou have successfully transferred a sum of N{amount} to,\nAccount number: {beneficiary_num}\nBank Name: Polaris Bank")
                                            elif transfer_confirmation == "No":
                                                print("Please, start over again")
                                            else:
                                                print("Please, Enter the correct value")
                                        else:
                                            print("Incorrect pin")
                            else:
                                print("Invalid Code")
                    else:
                        print("Invalid Code")
                else:
                    print("Please, make sure the previous pin and your current pin are the same")
            else:
                print("Your 6 digit card number is incorrect")
        else:
            print("the last digits of your card is below or over 6 characters")

    # =================
    # OPTION 2(Airtime)
    # =================

    elif selection == 2:
        last_card_digits_input = input("Welcome to 2026 M4ACE!\nPlease enter the last six digits of your Debit Card: ")
        pin_creation = int(input("Create Pin: "))
        pin_confirmation = int(input("Please, confirm your pin: "))

        if len(last_card_digits_input) == 6:
            if last_card_digits == last_card_digits_input:
                if pin_creation == pin_confirmation:
                    print("Pin Successfully created")
                else:
                    print("Please, make sure the previous pin and your current pin are the same")
            else:
                print("Your 6 digit card number is incorrect")
            print("\nSomething happens here")

        else:
            print("the last digits of your card is below or over 6 characters")

    # ==============
    # OPTION 3(Data)
    # ==============

    elif selection == 3:
        print("M4Ace Banking\nSelect purchase type\n1>Self\n2>ThirdParty")
        m4Ace_purchase_type = int(input("Purchase Type: "))
        if m4Ace_purchase_type == 1:
            print("M4Ace Banking\nYou are not registered on USSD")
        elif m4Ace_purchase_type == 2:
            print("M4Ace Banking\nYou are not registered on USSD")
        else:
            print("Invalid Input")

    elif selection == 4:
        print("Sorry, Nothing to see here")

    # =============
    # CHECK BALANCE
    # =============
    elif selection == 5:
        transaction_pin = input("Enter 4-digit PIN(default: 0000): ")
        if transaction_pin == "0000":
            print(f"Your account balance is: {Account_Balance}")
        else:
            print("Invalid Pin")
    elif selection == 6:
        print("Sorry, Nothing to see here")
    elif selection == 7:
        print("Sorry, Nothing to see here")
    elif selection == 8:
        print("Sorry, Nothing to see here")

    # ========
    # Exit App
    # ========
    elif selection == 0:
        print("\nThank you for using M4Ace USSD Banking Service\nGood Bye😊")
    else:
        print("Wrong input")
else:
    print("\nInvalid USSD Code, please input a correct code")
