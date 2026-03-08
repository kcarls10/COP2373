import re

# Function to validate a phone number
def validate_phone(phone):
    return bool(re.match(r"^\d{3}-\d{3}-\d{4}$", phone))

# Function to validate a social security number
def validate_ssn(ssn):
    return bool(re.match(r"^\d{3}-\d{2}-\d{4}$", ssn))

# Function to validate a zip code
def validate_zip(zip_code):
    return bool(re.match(r"^\d{5}$", zip_code))

# Main function
def main():

    phone = input("Enter a phone number: ")
    ssn = input("Enter a SSN: ")
    zip_code = input("Enter a zip code: ")

    if validate_phone(phone):
        print("Phone number is valid")
    else:
        print("Phone number is not valid")

    if validate_ssn(ssn):
        print("SSN is valid")
    else:
        print("SSN is not valid")

    if validate_zip(zip_code):
        print("Zip code is valid")
    else:
        print("Zip code is not valid")

if __name__ == '__main__':
        main()
