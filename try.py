# try:
#     user_age =int(input("Enter your age: "))
#     if user_age <0:
#         print("Age cannnot be negative.")
#     elif user_age <18:
#         print("You are a minor.")
#     else:
#         print("You are an adult.")
# except ValueError:
#     print("Invalid input. Please enter a valid age")




    # Write a programme that accepts, a user gender, if the user is male display"you are a male"



# try:
#     gender=str(input("Enter your gender: "))
#     if gender.lower() =="male":
#         print("You are a male.")
#     elif gender.lower() =="female":
#         print("You are a female.")
#     else:
#         print("Enter your actual gender")
# except ValueError:
#     print("Invalid.Enter a valid gender.")


# Accept a number and based on the number give the corresponding day of the week

try:
    num= int(input("Enter a number to get the corresponding day of the week: "))
    if num ==1:
        print("Monday")
    elif num==2:
        print("Tuesday")
    elif num==3:
        print("Wednesday")
    elif num==4:
        print("Thursday")
    elif num==5:
        print("Friday")
    elif num==6:
        print("Saturday")
    elif num==7:
        print("Sunday")
    else:
        print("The number you input must be between 1 to 7 or either 1 and 7")
except ValueError:
    print("Enter a valid number")