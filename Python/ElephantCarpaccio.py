# Develop a calculator that takes in an item quantity, item price, and user two-letter state code
# and calculates tax rate and discount. Use vertical slicing to define value.

def calculateTax(state_code, total_price):
    # if user input matches any of the states, re-assigns tax_rate. Otherwise, defaults to 6.35% - avg US sales tax
    tax_rate = 0.0635
    if state_code == 'NC':
        tax_rate = .0475
    elif state_code == 'VA':
        tax_rate = .053
    elif state_code == 'CA':
        tax_rate = .0725
    elif state_code == 'UT':
        tax_rate = .0610
    elif state_code == 'PA':
        tax_rate = .06

    print('Your tax rate is:', tax_rate * 100, '%')

    # calculates tax and returns modified total price
    total_price = total_price + (total_price * tax_rate)
    return total_price


def calculateDiscount(total_price):
    # if total price matches any of the ranges, re-assigns discount_rate. Otherwise, defaults to no discount
    discount_rate = 0.0
    if total_price >= 50000:
        discount_rate = 0.20
    elif 25000 <= total_price < 50000:
        discount_rate = 0.15
    elif 10000 <= total_price < 25000:
        discount_rate = 0.1
    elif 5000 <= total_price < 10000:
        discount_rate = 0.05

    print('Your discount is:', discount_rate * 100, '%')

    # calculates discount and returns modified total price
    total_price = total_price * (1 - discount_rate)
    return total_price


# ---- main
# First through Third vertical slice: user inputs
# Seventh vertical slice: error handling
items_input = input('How many items do you have? ')
while not items_input.isdigit() or int(items_input) <= 0:
    items_input = input('How many items do you have? ')
items_input = int(items_input)

price_input = input('What is the unit price per item? ')
while not price_input.isdecimal() or float(price_input) <= 0:
    price_input = input('What is the unit price per item? ')
price_input = float(price_input)

state_input = input('What is your two-letter state code? ')
while len(state_input) != 2:
    state_input = input('What is your two-letter state code? ')

# Fourth vertical slice: calculate order total
order_total = items_input * price_input
print('\nPre-tax order total: $', format(order_total, ',.2f'))

# Sixth vertical slice: define calculate discount function
# Discount rate has to modify order_total before tax is calculated, but was less valuable than tax calculation
order_total = calculateDiscount(order_total)
print('Pre-tax order total with discount: $', format(order_total, ',.2f'))

# Fifth vertical slice: define calculate state tax function
order_total = calculateTax(state_input, order_total)
print('Post-tax order total with discount: $', format(order_total, ',.2f'))
