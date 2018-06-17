# Name: Samantha Mackay
# Student Number: 3467946
# Subject: CSIT110

"""
Past Examination Paper
CSIT110 Fundamental Programming with Python

Autumn 2017
"""

# ===================================================================

# Question 1
# Write a program that uses meaningful variable names and produces a given output
# First and third columns must have left alignment and second column must have right alignment


# User Details

# User 1
username1 = "matt"
phone1 = "1234"
email1 = "ma777@code.org"

# User 2
username2 = "joe"
phone2 = "9823"
email2 = "mjoe@python.com"

# User 3
username3 = "lee"
phone3 = "3463"
email3 = "lee81@gmail.com"


# Display User Information
print("{0:<15}{1:>10}     {2:<25}".format("Username", "Phone", "Email"))

print("{0:<15}{1:>10}     {2:<25}".format(username1, phone1, email1))
print("{0:<15}{1:>10}     {2:<25}".format(username2, phone2, email2))
print("{0:<15}{1:>10}     {2:<25}".format(username3, phone3, email3))


# End of Question 1.

# ===================================================================

# Question 2
# Write a program that asks the user to enter two integers and displays the sum and product of them.
# The program should work as:
# Enter the first integer: 10
# Enter the second integer: 35
# The sum of 10 and 35 is 45
# The product of 10 and 35 is 350

# The program must use string concatenation to display the sum output line
# The program must use string format to display the output line


# Ask user to enter 2 integers
user_input = input("Enter the first integer: ")
number1 = int(user_input)

user_input = input("Enter the second integer: ")
number2 = int(user_input)

# Calculate Sum and Product
number_sum = number1 + number2
number_product = number1 * number2

# Display Sum (using String Addition)
print("The sum of " + str(number1) + " and " + str(number2) + " is " + str(number_sum) + ".")

# Display Product (using String Format)
print("The product of {0} and {1} is {2}.".format(number1, number2, number_product))


# End of Question 2.

# ===================================================================

# Question 3
# Write a program to calculate journal subscription prices and display result.


# Ask User Input
student_yn = input("Are you a student? (Y/N): ")
journal1_yn = input("Subscribe to Journal of Algebra? (Y/N): ")
journal2_yn = input("Subscribe to Journal of Geometry? (Y/N): ")
journal3_yn = input("Subscribe to Journal of Number Theory? (Y/N): ")

cost = 0

if (student_yn == "Y"):
    # Yes, IS student

    if (journal1_yn == "Y"):
        cost = cost + 30

    if (journal2_yn == "Y"):
        cost = cost + 35

    if (journal3_yn == "Y"):
        cost = cost + 40

else:
    # No, NOT a student

    if (journal1_yn == "Y"):
        cost = cost + 50

    if (journal2_yn == "Y"):
        cost = cost + 60

    if (journal3_yn == "Y"):
        cost = cost + 70


# Display the Cost
print("The total cost is: $".format(cost))


# End of Question 3.

# ===================================================================

# Question 4
# Write a program using for loop to take a user input and display a times table


# Get User Input
user_input = input("Enter an integer: ")

entered_number = int(user_input)


# Display the Heading
print("Times table by {0}".format(entered_number))

# Display the Times Table
for i in range(1, 11):
    print("{0} x {1} = {2}".format(entered_number, i, entered_number * i))


# End of Question 4.

# ===================================================================

# Question 5
# Write a program to while loop a user input and summation until quit


# Initialise the sum as 0
sum_of_number = 0

# Run forever until user quit
while True:
    user_input = input("Enter an integer or q to quit: ")

    if (user_input == "q"):
        break

    number = int(user_input)

    # add the number to the sum
    sum_of_number = sum_of_number + number


# Display the sum
print("The sum is {0}".format(sum_of_number))


# End of Question 5.

# ===================================================================

# Question 6
# Determine the outcome of given code:

list2d = [
    [1, 2, 3, 4],
    [9, 8, 7, 6]
]

a = list2d[0][2] + list2d[1][0]

print(a)


# first index is row number, second index is column number

# therefore list2d[0][2] is:
# 0 row and 2 column = 3

# list2d[1][0]: 1 row 0 column = 9

# Therefore a = 3 + 9


# End of Question 6.

# ===================================================================
