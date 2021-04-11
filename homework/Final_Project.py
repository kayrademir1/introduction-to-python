a=0
print("Welcome toooo Who Wants to Be a Python Programmer?")
#We printed explanaition with this code.
q1=str(input("Question 1: What print code do?\nA: Makes loop\nB: Writes everything\nC: İt cant do anything with writing more code.\nD: It exports code.\n>>>"))
#We write code with this.
if q1=="b":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
q2=str(input("2) İf makes loops.\nA: True\nB: False\n>>>"))
if q2=="b":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
q3=str(input("3) We use ____ to make loops.\nA: print\nB: import\nC: else\nD: for/while\n>>>"))
if q3=="d":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
q4=str(input("4) We use ____ to making unlimited loops.\nA: While\nB: For\nC: İmport\nD: Print\n>>>"))
if q4=="a":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
q5=str(input("5) We use ___ to make games.\nA: Pygame\nB: Pandas\nC: Numpy\nD: Turtle\n>>>"))
if q5=="a":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
q6=str(input("6) We use IDE's for...\nA: Writing codes.\nB: Debugging codes\nC: Testing codes\nD: We don't use\n>>>"))
if q6=="a" and "b":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
q7=str(input("7) We use ___ to make calculator.\nA: Pandas\nB: Numpy\nC: Pygame\n>>>"))
if q7=="b":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
q8=str(input("8) Python created by___\nA: Guido van Rossum\nB: Bill Gates\nC: Elon Musk\nD: No one:)\n>>>"))
if q8=="a":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
q9=str(input("9) We use ___ to make conditions.\nA: İf\nB: For\nC: While\nD: Not\n>>>"))
if q9=="a":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
q10=str(input("Last question) We use ___ to add new libraries.\nA: İmport\nB: Pip install\nC: Print\nC: Not\n>>>"))
if q10=="a" and "b":
    print("Yeah! You take 10 points.!")
    a+=10
else:
    print("Oh! You can't take any points.!")
print("Tournament is finished! It is your point:",a)