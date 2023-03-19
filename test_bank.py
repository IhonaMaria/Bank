#Let's test bank.py code!

from bank_class import Bank
from bank import validate

def test_deposit():
    bank_prueba=Bank()
    bank_prueba.deposit(1000)
    assert bank_prueba.capacity==2000


def test_withdraw():
    bank_prueba=Bank()
    bank_prueba.deposit(1500)
    bank_prueba.withdraw(500)

    assert bank_prueba.capacity==2000

def test_validate():
    assert validate(r'49342234L')==True
    assert validate(r'33333333S')==True
    assert validate(r'3r6y667yf')==False
    assert validate(r'34678898h')==False
    assert validate(r'R45678812')==False



#To run the test:

 #You must be in the correct directory! (If not use cd to change directory)
 #pytest test_bank.py

