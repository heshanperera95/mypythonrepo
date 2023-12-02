print("Helllo This is first application")

unit_price =input ("enter unit price : ")
qty = input ("enter the qty : ")

total = float(unit_price)* int(qty)

print (" total is : ", total)


if total <1000 :
    print ("total is less than 1000")

else :
    if total<2000:
        print ("total is less than 2000")
    else:
        print ("Total is greater than 2000")
             