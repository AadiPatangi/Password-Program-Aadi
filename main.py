#static variable
TOTAL_NUMBER_OF_RULES = 2 #total number of rules going to be checked
NUMBERS = "0123456789"
SPECIALCHARACTERS = "!@#$%^&*()"
CAPITALLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASELETTERS = "abcdefghiklmnopqrstuvwxyz"
NAME = input("Enter your name: ")
BIRTHDAY = input("Enter your Birthday month: ")
residence = input("Enter your city of residence: ")
rulesMet = 0 #count the number of rules met by the password given

while rulesMet != TOTAL_NUMBER_OF_RULES:
    password = input("Please give me a password: ")
    rulesMet = 0 #reset the number of rules met

    #rule 1
    if len(password)>=12:
        #print("Good work!  Your password has enough characters.")
        rulesMet += 1
    else:
        print("It's too short! Has to contain at least 12 characters")

    #rule 2
    found = False 
    for n in NUMBERS:
        if n in password:
            rulesMet += 1
            #print("Good work!  Your password contains a number.")
            found = True
            break
    if found == False:
        print("Your password does not contain a number.")
    #rule3
    found = False
    for n in SPECIALCHARACTERS:
        if n in password:
          rulesMet += 1
          #print("Good Work! Your password contains a number")
          found = True
          break
    if found == False:
        print("Your password does not contain a special character")
    #rule4
    found = False
    for n in CAPITALLETTERS:
       if n in password:
         rulesMet += 1
         #print("Good Work! Your password contains a capital letter")
         found = True
         break
    if found == False:
      print("Your password does not contain a capital letter")
    #rule5
    for n in LOWERCASELETTERS:
      if n in password:
        rulesMet += 1
        #print("Good work! Your password contains a lowercase letter")
        found = True
        break
    if found == False:
      print("Your password does not contain a lowercase letter")
    #rule6
    for n in NAME:
      if n not in password:
        rulesMet += 1
        #print("Good work! Your password does not include your name")
        found = True
        break
    if n in password:
      print("Your pasword should not include your name")
    #rule7
    for n in NAME:
      if n != password:
        #print("Good work! Your name is not your password")
        rulesMet += 1
        found = True
        break
    if n == password:
      print("Your name cannot be your password")
    #rule8
    for n in BIRTHDAY:
      if n not in password:
        #print("Good work! Your password does not contain your birthday month ")
        rulesMet += 1
        found = True
        break
    if n in password:
      print("Your password should not include your birthday")
    #rule9
    for n in residence:
       if n not in  password:
      #print("Good work! Your password does not contain your city of residence")
        rulesMet += 1
        found = True
        break
    if n in password:
      print("Your password should not contain your city of residence ")

    if rulesMet == 9:
       print("Good work! Your password meets all the requirements")
       break

    
    