#                                    Welcome to { Laxmi Chit Fund }...

#  Basic Structure for Error Printing...
def error(x):
    
    if str(x) == "pin":
        for i in range(4):
            print("")
        print("Incorrect PIN".center(100))
        for i in range(4):
            print("")
        print(":===>   Papa ka naam tho yaad h na???   <===:".center(100))
        for i in range(10):
            print("")




def bank():                         
    
             #DATA FORMAT == "abhay:1234:1000_kaushal:6969:5000_nishchal:1515:500"
    c = True
    while c:
        # Data Debugging for file "bank.txt"---------------------------------------------------------------
        f = open("bank.txt","r")
        f.seek(0)
        all_data = f.read()
        f.close()
        
        if all_data == "":
            all_data = "abhay:0000:1000"
        #print("all_data :",all_data)

        # Data Stored in list for further use--------------------------------------------------------------
        all_acc=[]
        all_pin=[]
        all_amo=[]
        for i in all_data.split("_"):
            t=str(i).split(":")
            
            all_acc.append(t[0])
            all_pin.append(t[1])
            all_amo.append(t[2])
            
        '''
        print(all_acc)
        print(all_pin)
        print(all_amo)error("pin")
        '''
        for i in range(5):
            print("")
        print("Welcome to { Laxmi Chti Fund }...".center(100))
        for i in range(5):
            print("")
        print("1. Enter Account Detail                            2. Create Account     ".center(100))
        n = int(input("                              Enter Your Selection:"))
        for i in range(32):
            print("")
        
        if n==1:
            
            account = str(input("                              Enter Your Account No. :"))
            if account not in all_acc:
                print("Account Number does not exist...")
                #bank()
            else:
                for i in range(30):
                    print("")
                ap = all_acc.index(account)
                print(f"                       Hi {account}")
                for i in range(5):
                    print("")
                print("1. Withdrawal                                  4. Deposite       ".center(100))
                print("2. Mini Statement                              5. Balance Enquary".center(100))
                print("3. PIN Change                                  6. Other Services ".center(100))
                for i in range(18):
                    print("")
        
                a = int(input("                              Enter your selection:"))
                for i in range(30):
                    print("")
        

                if a==1 :
                    amount = int(input("                              Enter Your Ammount:"))
                    pin = str(input("                              Enter Your PIN:"))
                    if pin in all_pin:
                        pp0 = all_pin.index(pin)
                        ap0 = all_acc.index(str(account))
                        amo_in = all_amo[pp0]
                        nex = 0
                        if amount > int(amo_in) and ap0 == pp0:
                            for i in range(4):
                                print("")
                            print("Insufficient Balance.".center(100))
                            print("OOOTAAAT ME...".center(100))
                            for i in range(10):
                                print("")
                            nex = 1
                            #bank()
                    
                        if pp0 == ap0 and nex == 0:
                            for i in range(4):
                                print("")
                            print("Me na de ra....".center(100))
                            print("Jaa".center(100))
                            c = False
                            t = int(all_amo[pp0]) - amount
                            all_amo[pp0] = str(t)
                            for i in range(10):
                                print("")
                    else:
                        error("pin")
                        #bank() 
                         

                
                
                elif a==2 :
                    for i in range(20):
                        print("")
                    print("Sueeeeeeeeee...".center(100))
                    for i in range(15):
                        print("")
                    #bank()
                elif a==3 :
                    print("                              Enter Your Current PIN:")
                    pin = str(input())
                    if pin in all_pin:
                        ap1 = all_acc.index(account)
                        pp1 = all_pin.index(pin)
                        if ap1 == pp1:
                            new_pin2 = str(input("                              Enter your new PIN:"))
                            new_pin3 = str(input("                              Enter your new PIN:"))
                            if new_pin2 == new_pin3:
                                all_pin[pp1] = new_pin2
                                print("PIN Changed Successfully...".center(100))
                                c = False
                            else:
                                error("pin")
                                #bank()
                        else:
                            error("pin")
                            #bank()
                    else:
                        error("pin")
                        #bank()
                
                elif a==4 :
                    amount = str(input("                              Enter Your Ammount:"))
                    pin = str(input("                              Enter Your PIN:"))
                    if pin in all_pin:
                        pp0 = all_pin.index(pin)
                        ap0 = all_acc.index(account)
                        if ap0 == pp0:
                            print("Bus itne hi???".center(100))
                            all_amo[pp0] = str(int(all_amo[pp0]) + int(amount))
                            c = False
                            
                        else:
                            error("pin")
                            #bank()
                    else:
                        error("pin")
                        #bank()
                
                elif a==5 :
                    pin = str(input("                                   Enter your PIN:"))
                    if pin in all_pin:
                        pp4 = all_pin.index(pin)
                        ap4 = all_acc.index(account)
                        if ap4 == pp4:
                            for i in range(5):
                                print("")
                            print("Your Account Balance is :".center(100))
                            print(str("$"+str(all_amo[ap4])+"/-").center(100))
                            for i in range(10):
                                print("")
                            c = False
                            
                    else:
                        error("pin")
                        #bank()
                
                elif a==6 :
                    print("ERROR Code:Aarkas....\n Server3 Busy".center(100))
                    for i in range(10):
                        print("")

                    #bank()
                else:
                    print("Wait a Minute, Who are you".center(100))
                    
                
                
        if n==2:
            data=""
            cd=0
            d=0
            while(cd==0):
                new_acc = str(input("                        Enter Your desired Account No.(U_Rollno.) :"))
                if new_acc not in all_acc:
                    cd = cd+1
            while(d==0):
                new_pin = str(input("                              Enter Your desired PIN :"))
                if len(new_pin) != 4 and new_pin in all_pin:
                    print("Your Pin must be taken or less than 4 digit...".center(100))
                else:
                    d=1
            all_acc.append(new_acc)
            all_pin.append(new_pin)
            all_amo.append(0)
            print("Account Created...".center(100))
            c = False
            
            


        # DATA REBUGGING for file "bank.txt"---------------------------------------------------------------

        all_dat = ""
        
        for i in range(len(all_acc)):
            t=str(all_acc[i])+":"+str(all_pin[i])+":"+str(all_amo[i])+"_"
            all_dat = all_dat + t
            
        all_dat = str(all_dat[0:len(all_dat)-1])
        # print(all_dat)
        # DATA Re-Writting for file "Bank.txt"---------------------------------------------------------------

        f=open("bank.txt","w")
        f.write(str(all_dat))
        f.close()
    

    
        
        
        
        

    
bank()



    
# Bank account no. [name]
# money
# pin

# mini statement dates
# ohter services

# print("Abhay".center(100))

"""
a = "abhay:1234:1000_kaushal:6969:5000_nishchal:1515:500"
a.split("_")
['abhay:1234:1000', 'kaushal:6969:5000', 'nishchal:1515:500']
a=a.split("_")
a[0]
'abhay:1234:1000'
an = a[0].split(":")

an
['abhay', '1234', '1000']
int(an[2])
"""
