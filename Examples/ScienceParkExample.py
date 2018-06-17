# Example - Rewrite star gazing show

# print menu function


def print_menu():
    print("------------------------------------------------")
    print("          Welcome to Science Park!              ")
    print()
    print("Admission Charges: Adult $35, Child $20         ")
    print("Stargazing Show: $10/person                     ")
    print()
    print("Free Science Park Hats if you spend $150 or more")
    print("10% discount if you spend $200 or more          ")
    print("------------------------------------------------")
    print()
# End of function: "print_menu"

# Take order from user
# This function returns three values:
# (1) number of adults  (2) number of children
# (3) include star show or not


def take_order():
    print("Please make your order.")
    print()

    # ask number of adults
    adult_input = input("Enter number of adults: ")
    adult = int(adult_input)

    # ask number of children
    child_input = input("Enter number of children: ")
    child = int(child_input)

    # ask additional star show
    star_show_input = input("Add Stargazing Show: (Y/N) ")
    if ((star_show_input == "Y") or (star_show_input == "y")):
        include_star_show = True
    else:
        include_star_show = False

    return adult, child, include_star_show
# End of function: "take_order"


# Assign price values to price variables
ADULT_PRICE = 35
CHILD_PRICE = 20
SHOW_PRICE = 10

DISCOUNT_MIN = 200
# Minimum amount to qualify for discount
DISCOUNT_PCT = 10
# Quantity of discount percentage

FREE_HAT_MIN = 150
# Minimum cost to qualify for free hat


# print cost
def print_cost(adult, child, include_star_show):
    # calculate the total charge, no discount yet
    adult_cost = ADULT_PRICE * adult
    child_cost = CHILD_PRICE * child

    if (include_star_show):
        show_cost = SHOW_PRICE * (adult + child)
    else:
        show_cost = 0

    total_cost = adult_cost + child_cost + show_cost

    # calculate discount and final charge
    if (total_cost >= DISCOUNT_MIN):
        # eligible for discount
        final_cost = total_cost * (100 - DISCOUNT_PCT) / 100

        print("Total cost: ${0}".format(total_cost))
        print("Discount {0}%".format(DISCOUNT_PCT))

    else:
        # not eligible for discount
        final_cost = total_cost

    print()
    print("Final charge: ${0}".format(final_cost))

    # check Free Hat
    if (total_cost >= FREE_HAT_MIN):
        print("Please collect Science Park Hats at the counter.")

    print()
    print("Enjoy your day!!!")

# End of function: "print_cost"


# Main program:
# print menu to user
print_menu()

# take order from user
adult, child, include_star_show = take_order()

# print receipt to user
print_cost(adult, child, include_star_show)

# End of Science Park Example.
