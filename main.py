num = int(input("Enter the number: "))
t = num
numLen = 0
while t > 0:
    numLen = numLen+1
    t = (t/10)
    if numLen>4:
        numLen = int(numLen/2)
        chk = 0
        while num>0:
            rem = num%10
            if chk == numLen:
                midOne = rem
            elif chk==(numLen-1):
                midTwo = rem
            num = int(num/10)
            chk = chk+1
        prod = midOne*midTwo
        print("\nProducts of mid digits is" ,prod)
else:
        print("\nIt's not 4 or more than 4 digit number")