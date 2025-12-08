# to calculate your height multiplied by your weight， it is healthy or not. healthcare.
from email.quoprimime import body_check
import random
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
email = input("Enter your email: ")
city = input("Enter your city: ")
print("Hello, " + name + "!")
person = {
    "name": name,
    "age": age,
    "gender": gender,
    "email": email,
    "city": city
}
print(person)
confirm=""
while confirm != "yes":
    confirm = input("Is the personal information correct? (yes/no): ")
    if confirm == "yes":
        print("Thank you, Let's continue :) !")
    else:
        print("PLEASE CHECK")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in centimeters: "))
print("\nChoose operation:")
print("1. Subtraction (-)")
operation = input("Enter your choice (1): ")
if (operation == "1"):
    result = height - weight
    print(result)

body = result

if body > 110:
    print("You are underweight.")
elif 110 >= body >=90:
    print("You are in the healthy weight range.")
elif body < 90:
    print("You are overweight.")


fun_messages = [
    "let's do some fun things.",
    "Today is sunday.",
    "I'm so happy today!",
]
def random_fun_message():
    msg = random.choice(fun_messages)
    print("\nRandom fun message: ", msg, "\n")
random_fun_message()