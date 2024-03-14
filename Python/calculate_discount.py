def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        price = price - discount_amount
    return price

original_price = float(input("Enter the original price of the item:"))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

print("The final price after applying the discount is: ${:.2f}".format(final_price))