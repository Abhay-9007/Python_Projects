

#                                       This is a code.

'''
You are tasked with creating a simple inventory management system for a small store.
The system should allow users to add products, remove products, update product quantities,
search for products, and display all products.
'''
def printf(x):
    for i in range(15):
        print("")
    print(str(x).center(100))
    for i in range(15):
        print("")

        

def project():
    
    #                               This is All Data at BackEnd. 
    ID = [101,102,103,104]
    name = ["Apple","Pineapple","Banana","Guava"]
    price = [100,120,20,40]
    quantity = [4,1,12,6]
    
    print(ID)
    print(name)
    print(price)
    print(quantity)
    
    for i in range(12):
        print("")
    #basic User Instructions.
    print("1. Add a Product         ".center(100))
    print("2. Remove a Product      ".center(100))
    print("3. Update Product Quality".center(100))
    print("4. Search for a Product  ".center(100))
    print("5. Display All Product   ".center(100))
    for i in range(15):
        print("")

    op = int(input("                                        Enter Your Selection:"))

    if op == 1:
        addname = str(input("Enter Product name to Add: "))
        if addname in name:
            printf("Alrady In...")
        else:
            pri = int(input("Enter Price:"))
            qt = int(input("Enter Quantity:"))
            pk = ID[-1] + 1
            while pk in ID:
                if pk in ID:
                    pk = pk + 1
            ID.append(pk)
            name.append(addname)
            price.append(pri)
            quantity.append(qt)
            printf("Added...")
            print()#

            
    elif op == 2:
        p = str(input("Enter Product Name to Remove:"))
        if p in name:
            ind = name.index(p)
            name.pop(ind)
            price.pop(ind)
            quantity.pop(ind)
            ID.pop(ind)
            printf("Removed...")
        else:
            printf("Nigga we don't have it...")

            
    elif op == 3:
        p = str(input("Enter Product name:"))
        if p not in name:
            printf("We Don't Have it...")
        else:
            ind = name.index(p)
            quantity[ind] = int(input("Enter new Quantity:"))
        printf("Quantity Updated...")


    elif op == 4:
        p = str(input("Enter Product Name:"))

        if p in name:
            printf("We have it...")
        else:
            printf("We don't know that Exist...")


    elif op == 5:

        for i in range(15):
            print("")
        
        print("Name    ".center(18),"ID      ".center(18),"Price   ".center(18),"Quantity".center(18))
        print("")
        
        for i in range(len(name)):
            print(str(name[i]).center(18),str(ID[i]).center(18),str(price[i]).center(18),str(quantity[i]).center(18))

        for i in range(10):
            print("")
    else:
        printf("Invalid Input...")

    print(ID)
    print(name)
    print(price)
    print(quantity)


        
    
        


project()
