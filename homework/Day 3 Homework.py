print("Welcome to Login Application")
username=str(input("Enter your username>>>"))
password=str(input("Enter your password\n(Good passwords have 8+ characters.)>>>"))
if len(password)>=8:
    print("Good! You can enter this app.")
if len(password)<=8:
    print("You cant enter this app. Your password should have 8+ characters.")

