# If i want check my condition whether met or not then in that case
# i raise Exception or use Assert

ItemsInCart = 0

# after 2 items added in cart ItemsInCart must be equal to 2 if not my
# Test case should fail

if ItemsInCart != 2:
    # raise Exception("Products cart count not matching")
    pass

# we can use assert also

assert(ItemsInCart == 2)
