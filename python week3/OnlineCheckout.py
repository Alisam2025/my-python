# Online Shopping Checkout System

# Input variables
is_member = input("Are you a store member? (yes/no): ").lower() == 'yes'
has_coupon = input("Do you have a discount coupon? (yes/no): ").lower() == 'yes'
cart_total = float(input("Enter your cart total: $"))
wants_express_shipping = input("Do you want express shipping? (yes/no): ").lower() == 'yes'

# Conditional logic with OR
if is_member or has_coupon:
    discount = 0.10  # 10% discount
    print("You qualify for a 10% discount!")
else:
    discount = 0.0
    print("No discount applied.")

# Calculate new total
discounted_total = cart_total * (1 - discount)

# More conditional logic with OR
if cart_total > 100 or is_member:
    shipping_cost = 0
    print("You get free shipping!")
elif wants_express_shipping:
    shipping_cost = 15
    print("Express shipping added: $15")
else:
    shipping_cost = 5
    print("Standard shipping added: $5")

# Final total
final_total = discounted_total + shipping_cost
print(f"Your final total is: ${final_total:.2f}")
