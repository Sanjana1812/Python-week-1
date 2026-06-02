def validate_password(password):                      # function to validate password

errors = []

if len(password) < 8:                                  # minimum length
    errors.append("Minimum 8 characters")

if not any(char.isupper() for char in password):        # uppercase check
    errors.append("Missing uppercase letter")

if not any(char.islower() for char in password):        # lowercase check
    errors.append("Missing lowercase letter")

if not any(char.isdigit() for char in password):          # digit check
    errors.append("Missing number")

special = "!@#$%^&*"                                      # special character check

if not any(char in special for char in password):
    errors.append("Missing special character")

return {                                                # return final result
    "is_valid": len(errors) == 0,
    "errors": errors
}
print(validate_password("weak"))                  # testing values

print(validate_password("Weak123"))

print(validate_password("MySecure@1"))
