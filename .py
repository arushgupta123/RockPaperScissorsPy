import random
import datetime
time = datetime.datetime.now()

cases = ["","","","","","",""]



if time.hour < 12:
    print("Good morning! This is rock paper scissor game!")
elif 12 <= time.hour < 18:
    print("Good afternoon! THis is rock paper scissor game!")
elif time.hour > 18 or time.hour == 18:
    print("Good evening! This is rock paper scissor game!")
else:
    print("This is rock paper scissor game")

print("Type 'Rock', 'Paper', or 'Scissor'. Avoid using spacebar, do not mess around with capital letters. Type the exact word the way it is written in this line")
print("Have fun!")

ops = ["Rock", "Paper", "Scissor"]
x = input("What do you choose?\n")


op1 = ops[random.randint(0,2)]

print(op1)

if x == op1:
    print("Your "+ x + " neutralized the opponents " + op1)
    cases[0] = "N"
elif x == "Rock" and op1 =="Paper":
    cases[0] = "C"
elif x == "Rock" and op1 =="Scissor":
    cases[0] = "H"
elif x == "Paper" and op1 =="Scissor":
    cases[0] = "C"
elif x == "Paper" and op1 =="Rock":
    cases[0] = "H"
elif x == "Scissor" and op1 =="Paper":
    cases[0] = "H"
elif x == "Scissor" and op1 =="Rock":
    cases[0] = "C"

print(cases[0])



xa = input("What do you choose?\n")


op2 = ops[random.randint(0,2)]

print(op2)

if xa == op2:
    print("Your "+ xa + " neutralized the opponents " + op2)
    cases[1] = "N"
elif xa == "Rock" and op2 =="Paper":
    cases[1] = "C"
elif xa == "Rock" and op2 =="Scissor":
    cases[1] = "H"
elif xa == "Paper" and op2 =="Scissor":
    cases[1] = "C"
elif xa == "Paper" and op2 =="Rock":
    cases[1] = "H"
elif xa == "Scissor" and op2 =="Paper":
    cases[1] = "H"
elif xa == "Scissor" and op2 =="Rock":
    cases[1] = "C"

print(cases[1])

xb = input("What do you choose?\n")


op3 = ops[random.randint(0,2)]

print(op3)

if xb == op3:
    print("Your "+ xb + " neutralized the opponents " + op3)
    cases[2] = "N"
elif xb == "Rock" and op3 =="Paper":
    cases[2] = "C"
elif xb == "Rock" and op3 =="Scissor":
    cases[2] = "H"
elif xb == "Paper" and op3 =="Scissor":
    cases[2] = "C"
elif xb == "Paper" and op3 =="Rock":
    cases[2] = "H"
elif xb == "Scissor" and op3 =="Paper":
    cases[2] = "H"
elif xb == "Scissor" and op3 =="Rock":
    cases[2] = "C"

print(cases[2])



xc = input("What do you choose?\n")


op4 = ops[random.randint(0,2)]

print(op4)

if xc == op4:
    print("Your "+ xc + " neutralized the opponents " + op4)
    cases[3] = "N"
elif xc == "Rock" and op4 =="Paper":
    cases[3] = "C"
elif xc == "Rock" and op4 =="Scissor":
    cases[3] = "H"
elif xc == "Paper" and op4 =="Scissor":
    cases[3] = "C"
elif xc == "Paper" and op4 =="Rock":
    cases[3] = "H"
elif xc == "Scissor" and op4 =="Paper":
    cases[3] = "H"
elif xc == "Scissor" and op4 =="Rock":
    cases[3] = "C"

print(cases[3])




xd = input("What do you choose?\n")


op5 = ops[random.randint(0,2)]

print(op5)

if xd == op5:
    print("Your "+ xd + " neutralized the opponents " + op5)
    cases[4] = "N"
elif xd == "Rock" and op5 =="Paper":
    cases[4] = "C"
elif xd == "Rock" and op5 =="Scissor":
    cases[4] = "H"
elif xd == "Paper" and op5 =="Scissor":
    cases[4] = "C"
elif xd == "Paper" and op5 =="Rock":
    cases[4] = "H"
elif xd == "Scissor" and op5 =="Paper":
    cases[4] = "H"
elif xd == "Scissor" and op5 =="Rock":
    cases[4] = "C"

print(cases[4])





xe = input("What do you choose?\n")


op6 = ops[random.randint(0,2)]

print(op6)

if x == op6:
    print("Your "+ xe + " neutralized the opponents " + op6)
    cases[5] = "N"
elif x == "Rock" and op6 =="Paper":
    cases[5] = "C"
elif x == "Rock" and op6 =="Scissor":
    cases[5] = "H"
elif x == "Paper" and op6 =="Scissor":
    cases[5] = "C"
elif x == "Paper" and op6 =="Rock":
    cases[5] = "H"
elif x == "Scissor" and op6 =="Paper":
    cases[5] = "H"
elif x == "Scissor" and op6 =="Rock":
    cases[5] = "C"

print(cases[5])





xf = input("What do you choose?\n")


op7 = ops[random.randint(0,2)]

print(op7)

if xf == op7:
    print("Your "+ xf + " neutralized the opponents " + op7)
    cases[6] = "N"
elif xf == "Rock" and op7 =="Paper":
    cases[6] = "C"
elif xf == "Rock" and op7 =="Scissor":
    cases[6] = "H"
elif xf == "Paper" and op7 =="Scissor":
    cases[6] = "C"
elif xf == "Paper" and op7 =="Rock":
    cases[6] = "H"
elif xf == "Scissor" and op7 =="Paper":
    cases[6] = "H"
elif xf == "Scissor" and op7 =="Rock":
    cases[6] = "C"

print(cases[6])




print(cases)
resultC = 0
resultN = 0
resultH = 0

for i in cases:
    if i == "C":
        resultC += 1
    elif i == "H":
        resultH += 1
    elif i == "N":
        resultN += 1

print("\n\n\n")
print("     ******************      ")
print("Results:\n")
print("Computer won: " + str(resultC))
print("Human won:" + str(resultH))
print("Nullified rounds:"+str(resultN))