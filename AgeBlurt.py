# Hack's AGE BLURT
# The program will then identify what year you were born

# ___________________________________DEFINITIONS________________________________________________

# Import of local time and date from built in datetime module
from datetime import date

# today variable is printed (tool to troubleshoot for calculation)
today = date.today()
print("Today\'s Date is: ", today, '\n')

# Gets the user's name for use later.
User_Name = input('\nEnter your name:')

# loop will occur to force correct prompt for calculation
Loop = 1
# ____________________________________CALCULATION_______________________________________________

while Loop == 1:
    Loop2 = 1
    # Birthday_Check is used to calculate correct year
    # .lower changes case sensitivity to match the call no matter the format
    # Two If statements force correct input for function
    Birthday_Check = input('Has your birthday passed this year?\n').lower()

    # Loop 0 will end the program indicating a completed task
    # 'No' will subtract one from the year to give correct User birth year
    # Try and except will confirm the age entered is a number
    if Birthday_Check == 'no':
        while Loop2 == 1:
            User_Age = input('Please enter your age. >')
            try:
                User_Age = int(User_Age)
                Birth_Year = today.year - User_Age - 1
                Loop2 = 0
                print('Hello ', User_Name, ', you were born in ', Birth_Year, '!', sep='')
                Loop = 0
            except ValueError:
                print("This is not a number. Please enter a valid number!")
    # Loop 0 will end the program indicating a completed task
    # 'Yes' will keep the year true to give correct birth year
    # Try and except will confirm the age entered is a number
    if Birthday_Check == 'yes':
        while Loop2 == 1:
            User_Age = input('Please enter your age. >')
            try:
                User_Age = int(User_Age)
                Birth_Year = today.year - User_Age
                Loop2 = 0
                print('Hello ', User_Name, ', you were born in ', Birth_Year, '!', sep='')
                Loop = 0
            except ValueError:
                print("This is not a number. Please enter a valid number!")
