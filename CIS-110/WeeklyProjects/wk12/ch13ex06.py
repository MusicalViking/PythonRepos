"""
Program Name : ch13ex06
Program description : Keeps track of attendees aty a conference
Author: Arthur Belanger
Date created: 4-26-25
Notes:
"""
import time
import csv

divider = ("_ _ _ ")
print(divider * 3)

class Attendee():
    def __init__(self, name, company, state, email):
        self._name = name
        self._company = company
        self._state = state
        self._email = email

    def __str__(self):
        return f"{self._name}, {self._company}, {self._state}, {self._email}"

    def getEmail(self):
        return self._email

    def updateEmail(self, email):
        self._email = email

class Conference():
    def __init__(self, name):
        self._name = name
        self._attendees = []

    def addAttendees(self, name, company, state, email):
        self._attendees.append(Attendee(name, company, state, email))
    
    def deleteAttendees(self, name, company, state, email):
        for attendee in self._attendees:
            if (attendee._name == name and
                    attendee._company == company and
                    attendee._state == state and
                    attendee._email == email):
                self._attendees.remove(attendee)
                return
        print(f"Attendee with name '{name}', company '{company}', state '{state}', and email '{email}' not found.")

    def listAttendee(self):
        for attendee in self._attendees:
            print(attendee)



def main():
    myConference = Conference("Friends of Python")
    try:
        with open("attendees.csv", 'r') as file:
            file.readline()
            for line in file:
                data = line.rstrip('\n').split(',')
                if len(data) == 4:
                    myConference.addAttendees(data[0].strip(), data[1].strip(), data[2].strip(), data[3].strip())
                else:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print("Error: attendees.csv not found.")
        return

    print("\nCurrent Attendees: ")
    myConference.listAttendee()
    
if __name__ == '__main__':
    main()




    
    
print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - Program # ")
print(time.ctime())
    
