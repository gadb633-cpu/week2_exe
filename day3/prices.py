# Modules
# exe 1
VAT_RATE = 0.17

def add_vat(amount):
    return amount + VAT_RATE

def apply_discount(amount, percent):
    return VAT_RATE + (amount*(1-(percent/100)))

# exe 2
# from prices import *  # for to import all
# import prices # for to import the file
# import prices as p # tu do alias
