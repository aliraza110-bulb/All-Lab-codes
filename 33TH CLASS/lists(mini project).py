list=[1,2,3]
try:
    print("Original List",list)
    list.append(4)
    list.insert(1,5)
    list.remove(2)
    list=list[::-1]
    
    
    try:
        list.remove(10)
    except ValueError:
        print("Error 10 Is Not Present In List")

    print(f"The Length Of List Is:{len(list)}")
    print("Modified List",list)


except Exception as e:
    print("Error",e)
w
