
#WELCOME TO YOUR BANK!

#Check if the user is a customer of the bank:

import re
from bank_class import Bank



def main():

    if validate(input("Introduce ID to access the bank account: ")) :
        bankclass = Bank()
        bankclass.deposit(float(input('Insert the quantity you want to deposit in your account:')))
        bankclass.withdraw(float(input('Insert the quantity you want to withdraw from your account: ')))

        print(bankclass,'€')

        if ask_convert():
            # 1 eur = 1.17 dollars
            print(f"Your current deposit is now {bankclass.capacity*1.17:.2f}$")   #Using the :.2f format specifier to show only 2 decimal places for the converted amount.


def validate(ID):
    if re.search(r"^([0-9]{8}[A-Z]{1})$",ID):
        print('Welcome back, dear customer')
        return True
    else:
        print('Incorrect ID')
        return False


def ask_convert():
    if input('Would you like to convert your deposit to dollars? 1=YES, 0=NO  ')=='1':
        return True
    else:
        return False


if __name__ == '__main__':
    main()






