bruhmoment = []

bruh = True

while bruh == True:
    
    print ("Bruh.exe O_O")

    print ("1. Remove a Student")
    print ("2. Add a Student")
    print ("3. Update the list")
    print ("4. Check shit")



    bruh2 = int(input("Enter a number: "))

    if bruh2 == 1:
       name = input ("Remove a student: ")
       bruhmoment.remove(name)
       
    elif bruh2 == 2:
       name = input ("Enter a name: ")
       bruhmoment.append(name)
       

    elif bruh2 == 3:
        print(bruhmoment)
        aids = int(input("Which index?"))
        print("Change " + bruhmoment[aids] + " to?")
       

        adrian = input()
        bruhmoment[aids] = adrian

        print("Success.")

    elif bruh2 == 4:
        print(bruhmoment)
