p=int(input("Enter Loan Amount: "))
n=(int(input("Enter Number of Months: "))+1)
R=(int(input("Enter Interest Rate: ").replace("%","")))
balance=p
r=R/(n*100)
print(r)

EMI=p*r*((1+r)**n)/((1+r)**n-1)

for payment in range(1,n):
    balance=balance-EMI

    print("EMI: ",EMI)
    print("Balance: ",balance)
    print("--------")

