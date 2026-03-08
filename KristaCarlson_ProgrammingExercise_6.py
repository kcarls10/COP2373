import re

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