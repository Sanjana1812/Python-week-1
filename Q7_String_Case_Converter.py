def convert_case(text, case_type):       # function to convert string case
convert into uppercase                  
if case_type == "upper":
    return text.upper()

elif case_type == "lower":        # convert into lowercase
    return text.lower()

elif case_type == "title":          # convert into title case
    return text.title()

else:                              # invalid input
    return "Invalid case_type"

print(convert_case("hello world", "upper"))        # testing values

print(convert_case("HELLO WORLD", "lower"))

print(convert_case("hello world", "title"))

print(convert_case("hello", "caps"))
