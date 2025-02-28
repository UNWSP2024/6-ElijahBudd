# Elijah Budd
# 2/28/2025
# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

sales = float(input("Enter the total sales for the month: "))

def tax_rate():
    county_tax = sales * 0.025
    state_tax = sales * 0.05
    total_tax = county_tax + state_tax

    print(f"county tax: {county_tax:0.2f}")
    print(f"state tax: {state_tax:0.2f}")
    print(f"total sales tax: {total_tax:0.2f}")

if __name__ == '__main__':
    tax_rate()
