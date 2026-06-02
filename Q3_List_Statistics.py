def calculate_statistics(numbers):        # function to calculate statistics from list

if len(numbers) == 0:          # handle empty list

    return {
        "mean": 0,
        "max": None,
        "min": None,
        "count": 0
    }

result = {                # calculate values          
    "mean": sum(numbers) / len(numbers),
    "max": max(numbers),
    "min": min(numbers),
    "count": len(numbers)
}

return result

print(calculate_statistics([10, 20, 30, 40, 50]))    # testing values

print(calculate_statistics([]))
