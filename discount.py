price = 100.0

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (discount_percent / 100 * price)
        return discounted_price
    else:
        return price

final_price = calculate_discount(price, 20.0)
print("The final price is:", final_price)
