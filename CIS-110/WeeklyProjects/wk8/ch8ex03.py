"""
Program Name : ch8ex03
Program description : takes a set of words and makes an acronym from the first letters of the words
Author: Arthur Belanger
Date created: 3-27-25
Notes: This is the first time I have used .split()
"""
print("--------------------------------")
import time

def create_acronym(phrase):

  words = phrase.split() 
  acronym = ""
  for word in words:
    if word: 
      acronym += word[0].upper() 
  return acronym

phrase = input("Enter a phrase: ")
acronym = create_acronym(phrase)
print(f"The acronym is: {acronym}")

print("--------------------------------")
print("Arthur Belanger")
print("CIS-110 - ch8ex03 ")
print(time.ctime())
    

