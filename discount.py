price = 100.0
# discount_percent = 20.0

def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discounted_price = price - (discount_percent / 100 * price)

        return print("The final price is: ", discounted_price)
    else:
        return print("The final price is: ", price)

calculate_discount(price, 20.0)

#      OR

 
# if __name__ == "__main__":
#     discount_percent = 10.0
#     final_price = calculate_discount(price, discount_percent)
#     print(f"The final price after discount is: {final_price}")
