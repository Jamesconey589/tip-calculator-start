#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
message = input("Welcome to the tip calculator.\nWhat was the total bill? $")
bill = float(message)
message2 = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip = int(message2)
message3 = input("How many people to split the bill? ")
numpeople = int(message3)
finalproduct = (tip / 100 * bill + bill) / numpeople
print(f"Each person should pay: ${round(finalproduct, 2)}")

