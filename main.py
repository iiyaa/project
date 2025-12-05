# to calculate your height multiplied by your weight， it is healthy or not. healthcare.

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
confirm = input("Is the personal information correct? (yes/no): ")
if confirm == "yes": print("Thank you, Let's continue :) !")
else: print("PLEASE CHECK")



