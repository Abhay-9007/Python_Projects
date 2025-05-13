
#                                      This is Minesweeper Game                     Date = [12 Nov 2024]
import random as r
                    #Win incomplete...
                    #bomb marking fail...

def bombn(a,b,c,d,e,l1): # No. Filler into tiles {Working on it...}
    z=[]
    y=[]
    x=[]
    w=[]
    v=[]
    l=[] #Spare use
    
    for i in l1:
        if(int(i/5)==0):
            z.append(i)
        elif(int(i/5)==1):
            y.append(i-5)
        elif(int(i/5)==2):
            x.append(i-10)
        elif(int(i/5)==3):
            w.append(i-15)
        elif(int(i/5)==4):
            v.append(i-20)
        else:
            print("Something went Wrong...")
        
    bomb(l,a,b,z)
    bomb(a,b,c,y)
    bomb(b,c,d,x)
    bomb(c,d,e,w)
    bomb(d,e,l,v)

    #print(l,"l")

    print(z)
    print(y)
    print(x)
    print(w)
    print(v)
    
            
        
def bomb(f,b,l,bn): #Helper for bombn()
    
    for bx in bn:
        try:
            f[bx] = f[bx] + 1
        except:
            print("Chal gaya Shayad...")
        finally:
            print("Bomb has been Planted...")

        try:
            f[bx+1] = f[bx+1] + 1
        except:
            print("Chal gaya Shayad...")
        finally:
            print("Bomb has been Planted...")
            
        try:
            f[bx-1] = f[bx-1] + 1
        except:
            print("Chal gaya Shayad...")
        finally:
            print("Bomb has been Planted...")

        try:
            b[bx+1] = b[bx+1] + 1
        except:
            print("Chal gaya Shayad...")
        finally:
            print("Bomb has been Planted...")#

        try:
            b[bx-1] = b[bx-1] + 1
        except:
            print("Chal gaya Shayad...")
        finally:
            print("Bomb has been Planted...")
            
        try:
            l[bx] = l[bx] + 1
        except:
            print("Chal gaya Shayad...")
        finally:
            print("Bomb has been Planted...")

        try:
            l[bx+1] = l[bx+1] + 1
        except:
            print("Chal gaya Shayad...")
        finally:
            print("Bomb has been Planted...")

        try:
            l[bx-1] = l[bx-1] + 1
        except:
            print("Chal gaya Shayad...")
        finally:
            print("Bomb has been Planted...")




def printf(x,z):
    for i in range(37):
        if i == 27 and z!=0:
            print(z,end="")
        else:
            print(" ", end = "")
        
    for i in x:
        print(str(i).center(2), end = "   ")
    print("")
    print("")

def println(ia,a,b,c,d,e):

    for i in range(15):
        print("")
        
    printf(ia,0)
    print()
    print()
    print()
    printf(a,"A")
    printf(b,"B")
    printf(c,"C")
    printf(d,"D")
    printf(e,"E")

    for i in range(10):
        print("")

def mine():


    #Land Generation
    all_ln = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    all_bo = []
    flag = "⚡︎⚡︎"
    
    #bomb filling and there location storage
    while len(all_bo) != 4:
        t = r.randint(0,24)
        if t not in all_bo:
            all_bo.append(t)
            all_ln[t] = "*"

    '''        
    # test case : 1        
    all_ln = [0,0,"*",0,0,0,0,0,0,0,0,0,"*",0,0,0,0,0,0,0,0,0,0,0,0]
    all_bo = [2,12]
    '''
    
    #bomb_locator(all_ln,all_bo)  

    l0=[1,2,3,4,5]
    l1=all_ln[0:5]
    l2=all_ln[5:10]
    l3=all_ln[10:15]
    l4=all_ln[15:20]
    l5=all_ln[20:25]

    bombn(l1,l2,l3,l4,l5,all_bo)
    
    #basic Schema
    
    #println(l0,l1,l2,l3,l4,l5)
    #print(all_bo)
    
    #Bomb are set on tiles
    #And marking are given properly

    #Code time Nigger
    t1 = ['⌘','⌘','⌘','⌘','⌘']
    t2 = ['⌘','⌘','⌘','⌘','⌘']
    t3 = ['⌘','⌘','⌘','⌘','⌘']
    t4 = ['⌘','⌘','⌘','⌘','⌘']
    t5 = ['⌘','⌘','⌘','⌘','⌘']
    
    


    #While Loop Is implied here till not Solved...
    
    repeat = True
    while repeat:
        
        println(l0,t1,t2,t3,t4,t5)

        op = str(input("                                 Enter your Operation:"))
        col=op[0] #Column 'A'
        row=int(op[1])-1 #Row '1'

        try:
            fop = str(op[2])
            print("taken")
        except:
            print("Detected")

        
            

        #Retriving Element 
        chan = 0
        rown = 0
        if col=='a':
            chan = l1[row]
            rown = 1
        elif col=='b':
            chan = l2[row]
            rown = 2
        elif col=='c':
            chan = l3[row]
            rown = 3
        elif col=='d':
            chan = l4[row]
            rown = 4
        elif col=='e':
            chan = l5[row]
            rown = 5

        #End Condition
        if chan == '*':
            println(l0,l1,l2,l3,l4,l5)
            for i in range(3):
                print("")
            print("You Stepped on a Nischal's Mom".center(90))
            print("Game Over".center(90))
            
            repeat = False
        
        #Processing 0 Found
        elif chan == 0:
            if rown == 1:
                try:
                    t1[row] = l1[row]#change
                except:
                    print("")
                try:
                    t1[row-1] = l1[row-1]
                except:
                    print("")
                try:
                    t1[row+1] = l1[row+1]
                except:
                    print("")
                    
                try:
                    t2[row-1] = l2[row-1]
                except:
                    print("")
                try:
                    t2[row+1] = l2[row+1]
                except:
                    print("")
                try:
                    t2[row] = l2[row]
                except:
                    print("")

                    
            elif rown == 5:
                try:
                    t5[row-1] = l5[row-1]
                except:
                    print("")
                try:
                    t5[row+1] = l5[row+1]
                except:
                    print("")
                    
                try:
                    t4[row-1] = l4[row-1]
                except:
                    print("")
                try:
                    t4[row+1] = l4[row+1]
                except:
                    print("")
                try:
                    t4[row] = l4[row]
                except:
                    print("")

            elif rown == 2: #Copy |
                try:
                    t2[row-1] = l2[row-1]
                except:
                    print("")
                try:
                    t2[row+1] = l2[row+1]
                except:
                    print("")
                    
                try:
                    t3[row-1] = l3[row-1]
                except:
                    print("")
                try:
                    t3[row+1] = l3[row+1]
                except:
                    print("")
                try:
                    t3[row] = l3[row]
                except:
                    print("")

                try:
                    t1[row-1] = l1[row-1]
                except:
                    print("")
                try:
                    t1[row+1] = l1[row+1]
                except:
                    print("")
                try:
                    t1[row] = l1[row]
                except:
                    print("")
            
            elif rown == 3: #Copy |
                try:
                    t3[row-1] = l3[row-1]
                except:
                    print("")
                try:
                    t3[row+1] = l3[row+1]
                except:
                    print("")
                    
                try:
                    t4[row-1] = l4[row-1]
                except:
                    print("")
                try:
                    t4[row+1] = l4[row+1]
                except:
                    print("")
                try:
                    t4[row] = l4[row]
                except:
                    print("")

                try:
                    t2[row-1] = l2[row-1]
                except:
                    print("")
                try:
                    t2[row+1] = l2[row+1]
                except:
                    print("")
                try:
                    t2[row] = l2[row]
                except:
                    print("")
            
            elif rown == 4: #Copy |
                try:
                    t4[row-1] = l4[row-1]
                except:
                    print("")
                try:
                    t4[row+1] = l4[row+1]
                except:
                    print("")
                    
                try:
                    t5[row-1] = l5[row-1]
                except:
                    print("")
                try:
                    t5[row+1] = l5[row+1]
                except:
                    print("")
                try:
                    t5[row] = l5[row]
                except:
                    print("")

                try:
                    t3[row-1] = l3[row-1]
                except:
                    print("")
                try:
                    t3[row+1] = l3[row+1]
                except:
                    print("")
                try:
                    t3[row] = l3[row]
                except:
                    print("")     
                
            
                
                
        #Showing Element        
        else:
            if col=='a':
                t1[row] = l1[row]
            elif col=='b':
                t2[row] = l2[row]
            elif col=='c':
                t3[row] = l3[row]
            elif col=='d':
                t4[row] = l4[row]
            elif col=='e':
                t5[row] = l5[row]

        '''        
        if fop == "f":
            if col=='a':
                t1[row] = flag
            elif col=='b':
                t2[row] = flag
            elif col=='c':
                t3[row] = flag
            elif col=='d':
                t4[row] = flag
            elif col=='e':
                t5[row] = flag
        '''


        
mine()
