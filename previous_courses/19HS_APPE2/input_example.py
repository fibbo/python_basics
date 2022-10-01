answer = input("Do you like Python? (yes/no)")

answer = answer.strip()
answer = answer.lower()

if answer == "yes":
    print("Awesome")
else:
    print("Too bad")
