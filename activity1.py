medical_cause= (input("Do you have a medical cause (yes/no):"))

if medical_cause == "yes" :
    print ("You're allowed")
else:
    attendance= int(input("Enter attendance of student:"))
    if attendance >= 75 :
        print ("Allowed")
    else: 
        print ("You are not allowed")