# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: December 2019
# This program formats the mailing address using given input.


def format_address(first_name, last_name, street_add, city,
                   province, postal_code, apt_number=None):
    # returns formatted mailing address

    if apt_number is not None:
        address = first_name + " " + last_name + "\n" + apt_number + "-" \
          "" + street_add + "\n" + city + " " + province + " " + postal_code
    else:
        address = first_name + " " + last_name + "\n" + street_add + "\n" + \
             city + " " + province + " " + postal_code

    return address


def main():
    # this function gets user input and fromats it into mailing address.
    # welcome statement.
    print("")
    print("This program formats your mailing address using given input")
    print("Make sure all of your input is in upper case!")
    print("")

    apt_number = None

    # getting input from user
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    question = input("Does your receiver have an apartment number? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter the apartment number: ")
    street_add = input("Enter the street address: ")
    city = input("Enter the city: ")
    province = input("Enter the province: ")
    postal_code = input("Enter the postal code: ")

    # process

    if apt_number is not None:
        address = format_address(first_name, last_name, street_add, city,
                                 province, postal_code, apt_number)
    else:
        address = format_address(first_name, last_name, street_add,
                                 city, province, postal_code)

    # output
    print("")
    print(address)


if __name__ == "__main__":
    main()
