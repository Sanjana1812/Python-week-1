def separate_even_odd(numbers):        # function to separate even and odd numbers
even = []
odd = []
for num in numbers:             # checking each number
    if num % 2 == 0:            # even number
        even.append(num)
    else:                    # odd number
        odd.append(num)

return (even, odd)      # returning both lists

result = separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])        # testing values

print("even :", result[0])

print("odd :", result[1])
