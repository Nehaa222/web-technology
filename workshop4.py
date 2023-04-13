def multiplication_table():
    """"This is a doc string"""
    num=int(input("enter a number:"))
    for i in range(1,num+1):
        for j in range(1,num+1):
            result=i*j
            print(result,end=" ")
    print()

multiplication_table()

