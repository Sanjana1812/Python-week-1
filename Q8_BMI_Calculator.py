def calculate_bmi(weight_kg, height_m):    # function to calculate bmi and category

bmi = weight_kg / (height_m ** 2)      # bmi formula

bmi = round(bmi, 2)                # round to 2 decimal places

if bmi < 18.5:                    # check category
    category = "Underweight"

elif bmi <= 24.9:
    category = "Normal weight"

elif bmi <= 29.9:
    category = "Overweight"

else:
    category = "Obese"

return {                          # return result in dictionary
    "bmi": bmi,
    "category": category
}
print(calculate_bmi(70, 1.75))      # testing values

print(calculate_bmi(90, 1.75))

print(calculate_bmi(100, 1.75))
