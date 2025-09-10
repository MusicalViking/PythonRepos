"""
Author: Arthur Belanger
Program Name: StopAndShop.py
Program Description: Creating a program to learn the way functions are called and 
related to one another within one program, object oriented programming.
Program Structure Outline:
    Intro and welcome
    ask to continue and purpose
    if purpose a or purpose b redirect to proper verifications
    option a invloves three rooms and each with a question test to enter
    option b requires solving a problem to enter, once inside you have three rooms
    when in either a or b you will have the option to switch to the other
    ---
    you will start with a bank rool of $200
    you may buy food or drink in each room

    you may provide services that are called from a random list for more $
    at any time you may pay bill and or get paid
    while money is held you will collect interestbased on which room you are in
    money increases with each interaction
    sign out and leave with password to return, password gets extra $200 on return.
"""

import time

welcome = "Welcome to the Shop CIS club where you are able to perform all aspects of machine interactions."


def purchaseEquipment():
    print("You have chosen to make a purchase today, let's get started.")


def repairEquipment():
    print(
        "You have chosen to have a specific piece of equipment repaired, let's get started."
    )


def seekAssistance():
    print(
        "You have chosen to speak to one of our experts, is this about software or hardware?"
    )


def socialize():
    print("Welcome to the Tech HubSpot, a place where like minded people can hang.")


def qualityControl():
    print(
        "You have selected to be a part of our quality control department, Thanks, now let's test something."
    )


actions = {
    1: purchaseEquipment,
    2: repairEquipment,
    3: seekAssistance,
    4: socialize,
    5: qualityControl,
}


def main():
    response = int(
        input(
            "Please choose which best descibes your visit today:\n"
            "1. I would like to make a purchase."
            "2. I would like to have something repaired."
            "3. I am looking for advice from one of your experts."
            "4. I just want to hang with some fellow tech enthusiasts."
            "5. I would like to help test for quality control in your products."
        )
    )

    action = actions.get(response)
    if action:
        action()
    else:
        print("Invalid Choice, please select a number between 1 and 5.")


main()


print(time.ctime())
