#SSILENCE BIDDING SYESTEM
##Python Dictionaries
import os

def clear_screen() :
    os.system('cls' if os.name== 'nt' else 'clear')
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################

#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log[3] = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},]
# student_scores = {
#   "ron" : 78,
#   "hermoine": 99,
# }
# student_grades = {}
# for student in student_scores:
#   score = student_scores[student]
#   if score>90:
#     student_grades[student] = "outstanding"
#   elif score> 80:
#     stuent_grades[student] =  "Exceeds Expectation"
#   elif score>70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "fail"
# print(student_grades)
#INTERACTIVE CODING EC=XERCISE 2
#I HAVE DONE IT SUCCEZFULY
#but the soloution was diffrnet so check it again u can create a new dictionary and then append it to list
# def add_new_country(country,total_visits,cities_visited):
#   travel_log[2] = {"country" : country,
#                    "cities_visited" : cities_visited,
#                    "total_visits": total_visits,
#                    }
# add_new_country("Russia","2",["Moscow","Saint Paris"])
# print(travel_log)
#NOW CREATING THE AUCTION PROGRAM
#THE PROGRAM MAY BE DESIGNED ON REPLIT
from art import lofo
print(lofo)
Bids = {}
def find_highest(Bidding_record):
     winner = ""
     highest_bid = 0

     for bidder in Bidding_record:
       bid_amount =  Bidding_record[bidder]
       if bid_amount > highest_bid:
          highest_bid = Bidding_record[bidder]
          winner = bidder
     print(f"The winner is {winner} with a bid of $ {highest_bid}")

condition = True
while condition==True:
  name = input("What is you name ? \n")
  bid_price = int(input("what's your Bid ? \n"))
  Bids[name] = bid_price
  further = input("Do u want to continue ,yes or no")
  clear_screen()
  if further == "no":
    condition = False
    find_highest(Bids)


