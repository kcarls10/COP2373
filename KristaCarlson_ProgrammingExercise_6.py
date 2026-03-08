import re

def validate_phone(phone):

    pattern = re.compile("^[1-9][0-9]{9}$")

    if re.match(pattern, phone):
        return True
    else:
        return False

def validate_ssn(ssn):
    pattern = re.compile("^[1-9][0-9]{9}$")
    if re.match(pattern, ssn):
        return True
    else:
        return False

def validate_zip(zip_code):
    pattern = re.compile("^[1-9][0-9]{9}$")
    if re.match(pattern, zip_code):
        return True
    else:
        return False


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

main()