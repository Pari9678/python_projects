print ("Select your transport:")
print ("1. bike")
print ("2. car")

choice = int(input("Enter your choice:"))
if (choice==1):
    print ("What type of bike?")
    print ("1. Scooty")
    print ("2. Scooter")

    choice2 = int(input("Enter your choice2:"))
    if choice2==1:
        print ("You have chosen Scooty")
    else:
        print ("You have chosen Scooter")

elif (choice==2):
    print ("What type of car?")
    print ("1. Sedan")
    print ("2. XUV")
    
    choice3 = int(input("Enter your choice3:"))
    if choice3==1:
         print ("You have chosen Sedan")
    else:
        print ("You have chosen XUV")

else:
    print ("Wrong choice")