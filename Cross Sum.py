# This is a program of " Cross Sum "  lives  == 3;                  Date = 17th to 18th Dec 2024
import random as r

#Printing all at once...
def printall(l1,a,b,c,d,l2):
    for i in range(15):
        print("")
    printf(["A","B","C","D"]," "," ")
    printf(l1,"#"," ")
    print()
    printf(a,l2[0],"A")
    printf(b,l2[1],"B")
    printf(c,l2[2],"C")
    printf(d,l2[3],"D")
    for i in range(2):
        print("")
    
#Print Single Array at once...
def printf(a,b,c):
    for i in range(40):
        if i == 34:
            print(c+"   "+str(b) ,end="")
        print(" ",end="")
    for i in range(len(a)):
        print(a[i],end="    ")
    print("")
    print("")
    
# fixin' random position...
def g():
    b = r.randint(1,4)
    
    return b

# Function for cheaking all at once..\
def cheakall(a,b,c,d,w,x,y,z):
    if a==w and b==x and c==y and d==z:
        return True
    return False

# This is Main Program...
def main():

    la=[0,0,0,0]

    l1=[0,0,0,0]
    l2=[0,0,0,0]
    l3=[0,0,0,0]
    l4=[0,0,0,0]
    
    lb=[0,0,0,0]

    for i in range(2):
        l1[g()-1] = g()
        l2[g()-1] = g()
        l3[g()-1] = g()
        l4[g()-1] = g()
    #Coping data for ans...

    a1 = [0,0,0,0]
    a2 = [0,0,0,0]
    a3 = [0,0,0,0]
    a4 = [0,0,0,0]
    
    for i in range(4):
        a1[i] = l1[i]
        a2[i] = l2[i]
        a3[i] = l3[i]
        a4[i] = l4[i]
        
    #print(cheakall(l1,l2,l3,l4,a1,a2,a3,a4))
    #print(l1,a1)

    l1sum = 0
    l2sum = 0
    l3sum = 0
    l4sum = 0

    for i in l1:
        l1sum = l1sum + i
    for i in l2:
        l2sum = l2sum + i
    for i in l3:
        l3sum = l3sum + i
    for i in l4:
        l4sum = l4sum + i
    
    lb = [l1sum, l2sum,l3sum,l4sum]
    
    for i in range(4):
        sex = l1[i]+l2[i]+l3[i]+l4[i]
        la[i] = sex
        
    for i in range(len(l1)):
        if l1[i] == 0:
            l1[i] = g()
        if l2[i] == 0:
            l2[i] = g()
        if l3[i] == 0:
            l3[i] = g()
        if l4[i] == 0:
            l4[i] = g()
    #print(l1,a1)    

    printall(la,a1,a2,a3,a4,lb)

    #printall(la,l1,l2,l3,l4,lb)

    c=3
    while c!=0:
        if cheakall(l1,l2,l3,l4,a1,a2,a3,a4):
            break
        
        printall(la,l1,l2,l3,l4,lb)
        print(f"Lives = {c}".center(92))
        #print(cheakall(l1,l2,l3,l4,a1,a2,a3,a4))
        for i in range(10):
            print()
        #Taking the input...   Format = "ab"
        op = str(input("                                  Enter Your input :")) # this is only for erase not for markin'

        intx = 0                                     # this is the index of that element 
        anst = []                                    # this is the element in ans list
        usert = []                                   # this is the element in user list
        tname = 0

        # Extrating index from input
        if op[-1] == 'a':
            intx = 0
        elif op[-1] == 'b':
            intx = 1
        elif op[-1] == 'c':
            intx = 2
        elif op[-1] == 'd':
            intx = 3
        else:
            print("Invalid Input...".center(100))

        # Extrating element from ans and user list using index    
        if op[0] == 'a':
            tname = 1
            anst = a1[intx]
            usert = l1[intx]
        elif op[0] == 'b':
            tname = 2
            anst = a2[intx]
            usert = l2[intx]
        elif op[0] == 'c':
            tname = 3
            anst = a3[intx]
            usert = l3[intx]
        elif op[0] == 'd':
            tname = 4
            anst = a4[intx]
            usert = l4[intx]
        else:
            print("Invalid Input...".center(100))
            
        # Processin' the input...
        if anst == usert:
            c = c - 1
            if c==0:
                print("You ran out of lives...".center(92))
                for i in range(5):
                    print()
                printall(la,a1,a2,a3,a4,lb)
                
        # Marking it 0
        elif anst == 0:
            if tname == 1:
                l1[intx] = 0
            elif tname == 2:
                l2[intx] = 0
            elif tname == 3:
                l3[intx] = 0
            elif tname == 4:
                l4[intx] = 0
        else:
            print("Something is off...".center(100))

            
    # Giving it an End...
    for i in range(15):
        print()
    print("Congratulation".center(100))
    print("You Win".center(100))
    for i in range(15):
        print()
            

    
main()    
