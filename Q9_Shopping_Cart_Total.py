def calculate_total(prices, discount_percent=0):              # function to calculate shopping total

subtotal = sum(prices)                                        # calculate total price

discount_amount = (subtotal * discount_percent) / 100        # calculate discount

final_total = subtotal - discount_amount      # final amount after discount

return {                                    # return result
    "subtotal": subtotal,
    "discount_amount": discount_amount,
    "final_total": final_total
}

print(calculate_total([50, 30, 45, 25]))      # testing values

print(calculate_total([50, 30, 45, 25], 10))

print(calculate_total([50, 30, 45, 25], 20))
