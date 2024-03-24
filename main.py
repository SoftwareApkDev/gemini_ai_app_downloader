"""
This file contains code for the application "Gemini AI App Downloader.
Author: SoftwareApkDev
"""


# App version: 0.5


# Importing necessary libraries


import os
import sys


# Creating static functions


def install_app(app_name):
    # type: (str) -> bool
    apps_file = open("apps.txt", 'r')
    apps: list = [app.strip() for app in apps_file]
    if app_name not in apps:
        return False

    os.system("pip3 install " + str(app_name))
    os.system("pip3 install " + str(app_name) + " --target installed/" + str(app_name))
    return True


def uninstall_app(app_name):
    # type: (str) -> bool
    installed_apps = [app for app in os.listdir("installed") if os.path.isdir(os.path.join("installed", app))]
    if app_name not in installed_apps:
        return False

    os.system("pip3 uninstall " + str(app_name))
    if sys.platform.startswith('win'):
        os.system("rmdir -r installed/" + str(app_name))  # For Windows System
    else:
        os.system("rm -r installed/" + str(app_name))  # For Linux System
    return True


def run_installed_app(app_name):
    # type: (str) -> bool
    installed_apps = [app for app in os.listdir("installed") if os.path.isdir(os.path.join("installed", app))]
    if app_name not in installed_apps:
        return False

    clear()
    os.system("python3 installed/" + str(app_name) + "/" + str(app_name) + "/" + str(app_name) + ".py")
    return True


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating main function used to run the application.


def main() -> int:
    """
    The main function used to run the application.
    :return: an integer
    """

    print("Welcome to 'Gemini AI App Downloader' by 'SoftwareApkDev'.")
    print("This application allows you to download apps with Google Gemini AI integrated into them and run them.")

    while True:
        print("Enter \"INSTALL APP\" to install an application.")
        print("Enter \"RUN INSTALLED APP\" to run an already installed application.")
        print("Enter \"UNINSTALL APP\" to uninstall an application.")
        allowed: list = ["INSTALL APP", "RUN INSTALLED APP", "UNINSTALL APP"]
        action: str = input("What do you want to do? ")
        while action not in allowed:
            clear()
            print("Enter \"INSTALL APP\" to install an application.")
            print("Enter \"RUN INSTALLED APP\" to run an already installed application.")
            print("Enter \"UNINSTALL APP\" to uninstall an application.")
            action = input("Sorry, invalid input! What do you want to do? ")

        if action == "INSTALL APP":
            clear()
            apps_file = open("apps.txt", 'r')
            apps: list = [app.strip() for app in apps_file]
            print("Below is a list of apps you can install:\n")
            for i in range(len(apps)):
                print(str(i + 1) + ". " + str(apps[i]))

            app_name: str = input("Please enter the name of the application you want to install: ")
            while app_name not in apps:
                app_name = input("Sorry, invalid input! Please enter the name of the application you want to install: ")

            install_app(app_name)

        elif action == "RUN INSTALLED APP":
            clear()
            installed_apps = [app for app in os.listdir("installed") if
                               os.path.isdir(os.path.join("installed", app))]
            print("Below is a list of installed games:\n")
            for i in range(len(installed_apps)):
                print(str(i + 1) + ". " + str(installed_apps[i]))

            app_name: str = input("Please enter the name of the application you want to run: ")
            while app_name not in installed_apps:
                app_name = input("Sorry, invalid input! Please enter the name of the application you want to run: ")

            run_installed_app(app_name)

        elif action == "UNINSTALL APP":
            clear()
            installed_apps = [app for app in os.listdir("installed") if
                              os.path.isdir(os.path.join("installed", app))]
            print("Below is a list of installed games:\n")
            for i in range(len(installed_apps)):
                print(str(i + 1) + ". " + str(installed_apps[i]))

            app_name: str = input("Please enter the name of the application you want to uninstall: ")
            while app_name not in installed_apps:
                app_name = input("Sorry, invalid input! Please enter the name of the application you want to "
                                 "uninstall: ")

            uninstall_app(app_name)

        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        continue_using: str = input("Do you want to continue using \"Gemini AI App Downloader\"? ")
        if continue_using != "Y":
            return 0


if __name__ == '__main__':
    main()
