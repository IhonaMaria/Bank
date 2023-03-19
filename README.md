# WELCOME TO YOUR BANK!

# Introduction

This is a program I made to consolidate the concepts I learnt from CS50 course introduction to programming with Python.

It simulates a situation where a new client wants to enter his account to deposit or withdraw money. First, the user is asked to enter his/her ID in order to check that the customer is indeed a client of the bank.
Then, the user decides the quantity to deposit or withdraw and the program outputs the deposit of the customer after the operations. Also, it has the option to convert the final deposit to dollars.

Moreover, the program has been tested out with pytest. 


# bank_classs

I created a class named Bank() and I incorprated the functions deposit and withdraw. I assumed that every new client starts with a deposit of 1000 eur. 
The deposit function adds a quantity (n) to the initial capacity deposit. 
The withdraw function removes a quantity (n) from the capacity added before. If the quantity the customer wants to withdraw is less than the quantity the customer has in the account, it raises a ValueError. 

# bank.py
 
First of all, through regular expressions, the program checks that the user correctly inserts the ID (8 numbers and a capital letter at the end). 
Then, the code imports the class previously mentioned and exits the final deposit of the customer in euros. 
Finally, it asks the user if he or she wants to convert the final quantity into dollars. The user has to answer binary  (1 for yes and 0 for no), and if he answers yes the proper conversion will appear. 

# test_bank.py

After developing the code, I designed another code to test it through pytest. I tested the deposit, withdraw and validate function. 


