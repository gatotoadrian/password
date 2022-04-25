#!/usr/bin/env python3.8

from secrets import choice
from user_login import User
from credentials import Credentials

def new_user(first_name, sur_name, user_name, email, password):
    '''
    Function using the User class to build a new_user
    Args:
    first_name: user's first name
    sur_name: user's surname
    user_name: user name to login
    email: email to login
    password: user's new password
    Returns: new_user
    '''
    new_user = User(first_name, sur_name, user_name, email, password)
    return new_user

def save_user(user):
    '''
    Function takes in the user returned above and saves it using the save_user method from the User class
    '''
    User.save_user(user)

def check_user(user_name, password):
    '''
    Function to see if the user exists in user_list
    '''
    check_user = Credentials.confirm_user(user_name, password)
    return check_user

def new_credentials(website_name, user_name, password):
    '''
    Function using the Credentials class to build a new_credentials
    Args:
    site_name: Website to which the credentials belong to
    user_name: The websites user_name
    password: The website's password
    Returns: new_credentials
    '''
    new_credentials = Credentials(website_name, user_name, password)
    return new_credentials

def save_credentials(credentials):
    '''
    function taking in the credentials and saving them to the credentials_list
    '''
    Credentials.save_credentials(credentials)

def list_credentials(user):
    '''
    Function calling the list_credentials method in Credntials to list credentials per user
    '''
    return Credentials.list_credentials(user)

def password_builder():
    '''
    function calling the password builder from Credentials class
    '''
    password = Credentials.password_builder()
    return password

def run():
    print(" ")
    print("*" * 80)
    print("WELCOME TO PASSWORD VAULT")
    print("*" * 80)
    while True:
        print(" ")
        print("=" * 80)
        print(" ")
        print(
            "Use the following options to navigate: \n 1 ==> Create an account \n 2 ==> Log In \n 3 ==> Exit"
        )
        choice = str(input("Enter option: "))
        if choice == "1":
            print("=" * 80)
            print(" ")
            print("Account Creation")
            print(" ")
            first_name = input("Enter your first name ==> ").strip()
            sur_name = input("Enter your surname ==> ").strip()
            user_name = input("Create your username ==> ").strip()
            email = input("Enter your email ==> ").strip()
            password = input("Enter your new master password ==> ").strip()
            save_user(new_user(first_name, sur_name, user_name, email, password))
            print(" ")
            print(
                f"Congratulations! A new account with the following credentials has been created: \n First Name: {first_name} \n Surname: {sur_name} \n Username: {user_name} \n Email: {email} \n Password: {password}"
            )
            print(" ")
            print(
                "Please note: The password above is your master password. Do not disclose it to anyone."
            )
        elif choice == "2":
            print("=" * 80)
            print(" ")
            print("Log Into Your Account")
            print(" ")
            user_name = input("Enter your username ==> ").strip()
            password = str(input("Enter your master password ==> "))
            username = check_user(user_name, password)
            if username == user_name:
                print(" ")
                print(
                    f"Welcome {user_name}. We are happy to have you \nSelect an option to continue: "
                )
                while True:
                    print(" ")
                    print(
                        "Pick an option: \n 1 ==> Save new credentials \n 2 ==> List saved credentials \n 3 ==> Return to main menu"
                    )
                    option = input("Enter an option: ").strip()
                    print(" ")
                    if option == "1":
                        print(" ")
                        print("Enter new credentials:")
                        website_name = input(r"Enter the website's name ==> ").strip()
                        user_name = input(r"Enter the website's account name ==> ")
                        while True:
                            print(" ")
                            print(
                                "Do you wish to generate a password or create one? \n 1 ==> Generete for me \n 2 ==> I'll create mine \n 3 ==> Return to previous menu"
                            )
                            choice = input("Enter your option: ")
                            print("=" * 80)
                            if choice == "2":
                                print(" ")
                                password = input("Enter your websites' password: ").strip()
                                break
                            elif choice == "1":
                                password = password_builder()
                                break
                            elif choice == "3":
                                break
                        save_credentials(new_credentials(website_name, user_name, password))
                        print(" ")
                        print(
                            f"New website information saved: \n Website: {website_name} \n Account Name: {user_name} \n Account Password: {password} "
                        )
                        print(" ")
                    elif option == "2":
                        print(" ")
                        if list_credentials(user_name):
                            print("Credentials: ")
                            print(" ")
                            for credentials in list_credentials(user_name):
                                print(
                                    f"Website: {credentials.site_name} \n Account Name: {credentials.user_name} \n Password: {credentials.password}"
                                )
                                print(" ")
                            else:
                                print(
                                    "We can't find any saved credentials under your account. Try selcting option 1 to save credentials before listing them"
                                )
                                print(" ")
                    elif option == "3":
                        break
            else:
                print(" ")
                print(
                    "invalid! Try chosing option 1 below to create an account"
                )
        elif choice == "3":
            print(" ")
            print("See you again soon!")
            break

if __name__ == "__main__":
    run()
