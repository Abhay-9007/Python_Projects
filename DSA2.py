def lib():
    #------------------------------------------------  Main Data Reading...
    data=""
    f=open("data.txt","r+")
    nd=f.read()
    for i in nd:
        if i in [" ","[","]",'"',"{","'","}"]:
            print("", end="")
        else:
            data=data+i
    data=data.split(",")
    #------------------------------------------------  Usrnames Reading...
    udata=""
    fdata=open("username_data.txt","r+")
    ndf=fdata.read()
    for i in ndf:
        if i in [" ","[","]",'"',"{","'","}"]:
            print("", end="")
        else:
            udata=udata+i
    udata=udata.split(",")
    usernames=udata
    #------------------------------------------------ Bio Reading...
    biodata=""
    fbiodata=open("biodata.txt","r+")
    bndf=fbiodata.read()
    for i in bndf:
        if i in [" ","[","]",'"',"{","'","}"]:
            print("", end="")
        else:
            biodata=biodata+i
    biodata=biodata.split(",")
    allbiodata=biodata
    #------------------------------------------------ Main Program...
    print("This is DSA_2.\n")
    while True:
        x=str(input("Choose only one \n[Sign In]:[S]\n[Log In]:[L]\n[Break]:[B]\n:"))
        if x=="l" or x=="L":
            ui=str(input("Enter your Username:"))
            pi=str(input("Enter your password:"))
            log=str(ui+":"+pi)
            if log in data:
                print("LogIn Successful...")
                inxed=usernames.index(ui)
                print("Your rank id no. =",inxed+1)
                print("Your Biodata is:\n",allbiodata[inxed])
            else:
                print("No data found.")
                print("Try Sign up.")
        elif x=="s" or x=="S":
            while True:
                uo=str(input("Enter your Username:"))
                po=str(input("Enter your password:"))
                if uo in usernames or len(po)<8:
                    print("Username already taken...")
                    print("Password must contain 8 digits.")
                else:
                    inp=str(uo+":"+po)
                    usernames.append(uo)
                    data.append(inp)
                    userbio=str(input("Enter your Bio:"))
                    allbiodata.append(userbio)
                    #------------------------------------------------  Main Data Writing...
                    fwrite=open("data.txt","w")
                    fwrite.write(str(data))
                    fwrite.close()
                    #------------------------------------------------  Username Writing...
                    fuwrite=open("username_data.txt","w")
                    fuwrite.write(str(usernames))
                    fuwrite.close()
                    #------------------------------------------------  Bio Writing...
                    fbwrite=open("biodata.txt","w")
                    fbwrite.write(str(allbiodata))
                    fbwrite.close()
                    print("Done...")
                    True
                    break


        elif x=="B" or x=="b":
            print("You have been successfully logged out.")
            print("Thank you...")
            f.close()
            fdata.close()
            True
            break


        elif x=="nigga":
            for i in range(5):
                print("")
            print(data)
            print(usernames)
            print(allbiodata)
            for i in range(15):
                if i==7:
                    print("                                              FUCK U God...")
                else:
                    print("")

        else:
            print("Whats the HURRY NIGGA...")
lib()
