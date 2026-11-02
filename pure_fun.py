# pure function
# exe 1
def square(n):  # pure
    return n * n
 
def log_square(n):   # pure
    print("squaring", n)
    return n * n
 
def add_item(cart, item):  # unpure side eppect is: change the "cart"
    cart.append(item)
    return cart
 
def with_item(cart, item):    # unpure side eppect is: change the "cart"
    return cart + [item]
