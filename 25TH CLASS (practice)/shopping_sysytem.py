cart=[]
while True:
    print("\n 1.add item \n 2.remove item \n 3.sort \n 4.count \n 5.print")

    choice=input("Enter Your Choice or type (stop) to finish : ")
    if choice == '1':
        item=input("Enter Name Of item : ")
        cart.append(item)
        print(f"{item} Has Been Added Sucessfully")

    elif choice == '2':
        item_rem=input("Enter Item Name To Remove : ")
        if item in cart:
            cart.remove(item)
            print(f"{item}Has Been Removed Sucessfully")
        else:
            print(f"{item_rem}Item Is not In cart")

    elif choice == '3':
        print(sorted(cart))
    

    elif choice == '4':
        count=len(cart)
        print("The Total Item In cart Is found To be : ",count)

    elif choice == '5':
        print("The Total Item in Your cart Are Following :",cart)
        
    else:
        if choice == 'stop':
            break


