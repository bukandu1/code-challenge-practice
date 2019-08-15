def nearestGreater(a):
    tuple_list = []
    b = []
    max = min(a)
    for i in range(0, len(a)):
        #create tuple list
        tuple_list.append((a[i], i))
    
    sorted(tuple_list)
    print(tuple_list)
    
    for i in range(0, len(a)):
        for index, num2 in enumerate(tuple_list):
            print(a[i], num2[0], index)
            if i == num2[1]:
                print("current index")
                continue

            elif a[i] == num2[0]:
                print("these are the same numbers. Continue.")
                continue

            elif a[i] < num2[0]:
                print("found a num larger!", a[i], num2[0])
                b.append(num2[1])
                break


        if i +1 != len(b):
            print("nothing larger")
            b.append(-1)
            
    return b

print(nearestGreater([1, 5, 10, 3, 4, 4]))
print(nearestGreater([100, 101, 1, 3, 4, 4]))